import sys
from time import sleep
import numpy as np
import pygame
from constants import *
from robot import *
from environment import *
from agent import *

#? Initialize environment
env = environment()
#? Initialize robot
robot = Robot()
#? Initialize the AI(?) 
robot_actor = Agent_actor()
robot_critic = Agent_critic()

for _ in range(epoch_length):
    #? Start playing
    reward = env.play_episode(robot, robot_actor)
    robot.tra

#? This loop is just for displaying the results of the "simulation" for the user(?) to see.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()