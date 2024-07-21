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
https://github.com/Cgamess/ut-game-engine
""" 
if 0: print(licence) # assigned it to a var and put it in a print statement to keep it in the code after compilation
import os
os.environ[r'PYGAME_HIDE_SUPPORT_PROMPTr'] = r"ut-game-engine: https://github.com/Cgamess/ut-game-engine"+"\n"+licence
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from PIL import Image
import numpy as np
import time
import json
from ntypes.ntypes import open_file_dialog
import subprocess
command=[r'.\pyinstaller.exe', r'--noconfirm', r'--onefile', r'--windowed', r'--name', r'"stuff"', r'--optimize', r'"2"', r'--add-data', r'"./myflag.png;."', r'--add-data', r'"./LICENSE.txt;."', r'--add-binary', r'"./binarys/opengl/SDL2.dll;."', r'--add-binary', r'"./binarys/basepython/python.exe;."', r'--add-binary', r'"./binarys/basepython/python3.dll;."', r'--add-binary', r'"./binarys/basepython/python312.dll;."',  r'"./runner.py"r']
subprocess.run(command)