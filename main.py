licence = r"""
Copyright 2024 Calvin Larsen:
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

The Rest in ./LICENCE
https://github.com/Cgamess/py-game-engine
""" 
if 0: print(licence) # assigned it to a var and put it in a print statement to keep it in the code after compilation
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = r"ut-game-engine: https://github.com/Cgamess/py-game-engine"+"\n"+licence
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from PIL import Image
import numpy as np
import time
import json
from ntypes.ntypes import open_file_dialog
from ntypes.calculations import calculate_width
pygame.init()

objects_list : list = []

info_object = pygame.display.Info()
screen_width = info_object.current_w
screen_height = info_object.current_h

# screen_width = 800
# screen_height = calculate_width((16,9),screen_width)
flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
screen = pygame.display.set_mode((screen_width, screen_height), flags)

while True:
    pass