# ! Colors
white = (255, 255, 255)
aqua= (0, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
silver = (192,192,192)
light_green = (152, 251, 152)

# ! Screen
screen_size = (800, 800)
screen_color = black
screen_delay = 10

# ! Constants related to the blocks
block_count = 5
block_size  = 40
block_color = green
block_positions = ((200, 600), (100,100), (100, 300), (400, 700), (600, 500), (500, 200))

# ! Robot
filename = "pic/character.gif"
starting_position = [screen_size[0]/2, screen_size[1]/2]
starting_rotation = 0
action = -1
robot_width = 40
robot_height = 40

# * RL Constants 
action_space = 4
reward_hit_wall = -50
reward_moving = 3
reward_turning = 3
reward_same_place = -10
#episode_length = 50000
episode_length = 5000
epoch_length = 1000
discount_lambda = 0.9995        #! Needs calibration!!!

#? Others
text_buffer = 10
text_box_width = 100; text_box_height = 50

# Required parameters
over = False
