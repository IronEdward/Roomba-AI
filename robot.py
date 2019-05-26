import pygame
import numpy as np
from constants import *

class Robot:
    def __init__(self):
        self.width      = robot_width
        self.height     = robot_height
        self.position   = starting_position
        #? Clockwise is positive, X-axis is 0 degrees.
        self.rotation   = starting_rotation
        self.image      = pygame.transform.scale(pygame.image.load(filename), (self.width, self.height))
        self.lin_speed  = 1
        self.rot_speed  = 1

    def forward(self, value, rect_list, disp_rect):
        """Defines linear motion. Forward is positive."""
        old_pos_x = self.position[0]; old_pos_y = self.position[1]
        self.position[0] += np.cos(np.deg2rad(self.rotation)) * value
        self.position[1] += np.sin(np.deg2rad(self.rotation)) * value
        self_rect = self.image.get_rect()
        self_rect.x = self.position[0] ;self_rect.y = self.position[1]
        for i in rect_list:
            if self_rect.colliderect(i) or not disp_rect.contains(self_rect):
                self.position[0] = old_pos_x; self.position[1] = old_pos_y
                self_rect.x = old_pos_x ;self_rect.y = old_pos_y

    def rotate(self, degree):
        """Defines rotation. Clockwise is positive. X-axis is 0 degrees."""
        self.rotation += degree
        if self.rotation > 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360