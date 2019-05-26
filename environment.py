import sys
import numpy as np
import pygame
from constants import *
from math import sqrt

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class environment():
    def __init__(self):
        pygame.init()
        self.disp = pygame.display.set_mode((screen_size), 0, 32)
        self.disp_rect = self.disp.get_rect()
        self.disp.fill(screen_color)
        self.rect_list = []
        # * Draw blocks
        for i,j in block_positions:
            self.rect_list.append(pygame.draw.rect(self.disp, block_color, (i, j, block_size, block_size)))

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def reset(self):
        # * Reset robot's position to starting position:
        robot.position = list(starting_position)
        score = 0
        return (int(robot.position[0]/block_size), int(robot.position[1]/block_size), robot.rotation, False)
    
    def reward(self, robot_min_coordinate_x, robot_min_coordinate_y, robot_max_coordinate_x, robot_max_coordinate_y):
        #? Reward function for the agent. 
        #? Reward = The amount of space the robot covered. Calculated by detecting each color of each pixel on the display surface.
        #? Not that efficient. There's probably a better way.
        #? Possible alternatives:
        #? 1. Memorize the space the robot has passed through. Use math and calculate it.
        #? 2. ......Cant think of anything rn. Hopefully sth comes up later.
        #? Gonna try out math for now.
        """
        for pixel_x in range(screen_size[0]):
            for pixel_y in range(screen_size[1]): 
                print(self.disp.get_at((pixel_x, pixel_y)))
        """
        #! Temporary solution: Calculate the rectangluar area of the area the robot passed through.
        reward = abs(robot_max_coordinate_x - robot_min_coordinate_x + robot_width) * abs(robot_max_coordinate_y - robot_min_coordinate_y + robot_width)
        pygame.draw.rect(self.disp, blue, (robot_min_coordinate_x, robot_min_coordinate_y, abs(robot_max_coordinate_x-robot_min_coordinate_x)+robot_width, abs(robot_max_coordinate_y-robot_min_coordinate_y)+robot_height))
        pygame.display.update()
        return reward


    def draw(self, robot, ticks):
        # * Draw robot
        self.disp.blit(rot_center(robot.image, -robot.rotation), robot.position) 

        #? Count for displaying the number of ticks passed from the beginning of the episode:
        pygame.draw.rect(self.disp, black, (0,screen_size[1] - text_box_height,text_box_width,text_box_height))
        textsurface = self.myfont.render(str(ticks), False, (255, 255, 255))
        self.disp.blit(textsurface,(text_buffer, screen_size[1] - text_box_height - text_buffer))
        pygame.display.update()

    def play_episode(self, robot, agent):
        #? For calculating reward at the end:
        robot_min_coordinate_x = screen_size[0]; robot_min_coordinate_y = screen_size[1]
        robot_max_coordinate_x = 0; robot_max_coordinate_y = 0

        #* This is gonna be considerably big. (episode_length * (x, y)) = 10000 numbers for now.
        action_reward = []
        for ticks in range(episode_length):
            #? robot_lin_action: linear speed
            #? robot_rot_action: rotation

            #! Q. How does the agent work?
            #! A. It's something close to solving a maze.
            #!    Basically, the agent doesn't get any reward up until the last timestep, where it gets a reward based on the amount of area it's covered.
            #!    The reward is going to go to all the actions taken in that episode, with a discount amount of "lambda", where the reward is reduced depending on how much it's pathed back.
            #!    ...if that makes sense.    
            #! Okay.
            #! Uh, so... for each timestep t^n, say the reward for timestep t^n is A. Then, timestep t^n-1(the previous timestep) will have a reward of A*"lambda" < A. 
            #! And that continues.
            
            
            #! Q. How does the reward reflect to the output of the Agent?
            #! A. Hmm....
            #!    So this is why regression and Reinforcement Learning aren't something you want to go together.....
            #!    I didn't want to use A3C or Policy Gradients, but I guess there's no choice.S 

            #! -------------------------Agent Configuration Starts-------------------------
            robot_action = agent.predict(robot.position)

            #? For debugging:
            #robot_action = 1
            #print(robot_action)

            #! -------------------------Agent Configuration Done---------------------------
            if robot_action == 0:
                robot.forward(robot.lin_speed, self.rect_list, self.disp_rect)
            elif robot_action == 1:
                robot.forward(-robot.lin_speed, self.rect_list, self.disp_rect)
            elif robot_action == 2:
                robot.rotate(-robot.rot_speed)
            elif robot_action == 3:
                robot.rotate(robot.rot_speed)

            rect_list = self.draw(robot, ticks)

            #? Stupid code but probably works.
            #? For x axis:
            if int(robot.position[0]) < robot_min_coordinate_x:
                robot_min_coordinate_x = int(robot.position[0])
            if int(robot.position[0]) > robot_max_coordinate_x:
                robot_max_coordinate_x = int(robot.position[0])
            
            #? For y axis:
            if int(robot.position[1]) < robot_min_coordinate_y:
                robot_min_coordinate_y = int(robot.position[1])
            if int(robot.position[1]) > robot_max_coordinate_y:
                robot_max_coordinate_y = int(robot.position[1])
            print(robot_min_coordinate_x, robot_min_coordinate_y, robot_max_coordinate_x, robot_max_coordinate_y)
        
        return self.reward(robot_min_coordinate_x, robot_min_coordinate_y, robot_max_coordinate_x, robot_max_coordinate_y)
    