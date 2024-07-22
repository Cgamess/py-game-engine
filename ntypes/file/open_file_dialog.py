import colorama
from collections import deque
from time import perf_counter_ns
import json
import tkinter as tk
from tkinter import filedialog
import numpy as np
import time
import json
tkroot = tk.Tk()
tkroot.withdraw()  # Hide the main window

def open_file_dialog(types=[("PNG files", "*.png")], title="Image"):
    
    file_path = filedialog.askopenfilename(filetypes=types, title=title)
    
    return file_path