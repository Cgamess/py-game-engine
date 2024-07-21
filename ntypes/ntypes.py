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

class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear       = _immutable
    update      = _immutable
    setdefault  = _immutable
    pop         = _immutable
    popitem     = _immutable

class render:
    init=0
    def __init__(self, size: list[int], cmap: dict, coloramt: int) -> None:
        self.init=0
        self.sizexy: list[int] = [0,0]
        self.size: int = 0
        if isinstance(size,list) and len(size)==2:
            self.sizexy: list[int] = size
            self.size: int = self.sizexy[0] * self.sizexy[1]
        else:
            if not isinstance(size,list):
                if len(size)!=2:
                    raise ValueError("arg size: length and type wrong")
                    exit()
                else:
                    raise ValueError("arg size: type wrong")
                    exit()
            else:
                if len(size)!=2:
                    raise ValueError("arg size: wrong length")
                    exit()
                else:
                    raise Exception("arg size: Unknown error")
                    exit()
        if len(cmap) != coloramt or coloramt <= 0:
            if len(cmap) != coloramt:
                raise ValueError("cmap/coloramt: cmap coloramt mismatch")
                exit()
            elif coloramt <=0:
                raise ValueError("arg coloramt: coloramt is zero or below")
                exit()
            else:
                raise Exception("arg cmap/coloramt: unknown error")
                exit()
        for i in cmap:
            if not isinstance(i,int):
                raise ValueError(f"arg cmap: key {i} in cmap is not an int")
                exit()
            if int(i) <= 0 or int(i) == 0:
                if int(i) == 0:
                    raise ValueError(f"arg cmap: key {i} cannot be 0")
                    exit()
                raise ValueError(f"arg cmap: key {i} cannot be 0 or less")
                exit()
            if not isinstance(cmap[i], dict):
                raise ValueError(f"arg cmap: {cmap[i]} at location {i} in cmap is not a dict")
                exit()
            keys=list(cmap[i].keys())
            if "Fore" not in keys:
                raise ValueError(f"arg cmap: {cmap[i]} at location {i} doesnt contain a Foreground (colorama.Fore.x or None)")
                exit()
            if "Back" not in keys:
                raise ValueError(f"arg cmap: {cmap[i]} at location {i} doesnt contain a Background (colorama.Back.x or None)")
                exit()
            if "Char" not in keys:
                raise ValueError(f"arg cmap: {cmap[i]} at location {i} doesnt contain a charicter (utf-8 or None)")
                exit()
        self.pxgrid: dict = {}
        for i in range(self.sizexy[0]):
            for j in range(self.sizexy[1]):
                self.pxgrid[(i,j)]=0
        self.cmap: dict = cmap
        self.init=1
        return(None)
    def Render(self):
        if not self.init:
            raise Exception("Needs to be initialized before you can render")
        for i in range(self.sizexy[1]):
            toprint: str = ""
            for j in range(self.sizexy[0]):
                if self.pxgrid[(j,i)]==0:
                    toprint+="??"
                else:
                    for k in self.cmap[self.pxgrid[(j,i)]]:
                        char=self.cmap[self.pxgrid[(j,i)]][k]
                        if char == None:
                            char=" "
                        toprint+=char
                    if char == None:
                        char+=" "
                    else:
                        try:
                            toprint+=self.cmap[self.pxgrid[(j,i)]]["Char"]
                        except:
                            toprint+=" "
                    toprint+=colorama.Back.RESET
                    toprint+=colorama.Fore.RESET
            toprint+=colorama.Back.RESET
            toprint+=colorama.Fore.RESET
            print(toprint)

class tlist(list):
    def _undefined():
        raise Exception("Error: undefined")
    def __init__(*stuff):
        super().__init__(stuff)
    # not done yet

class queue(tlist):
    def __init__(*stuff):
        super().__init__(stuff)
    def _undefined():
        raise Exception("Error: undefined")
    def ret(self):
        pass
    def swap(self):
        pass
    def pop(self):
        pass
    def retpop(self):
        var=self.ret()
        self.pop()
        return var


class jsonsavehandler:
    def __init__(self, path):
        self.basefile=open(path,"r+")
        self.path=path
    def refresh(self):
        self.basefile.close()
        self.basefile=open(self.path,"r+")
    def jsonread(self):
        tdata=self.read()
        data = json.loads(tdata)
        return data
    def read(self):
        self.refresh()
        return self.basefile.read()
    def write(self, data):
        self.basefile.write(data)
        self.basefile.flush
    def replace(self, data):
        self.olddata=self.jsonread()
        self.basefile.seek(0)
        self.basefile.truncate()
        self.write(data)
        self.basefile.flush()
    def jsonreplace(self, data):
        self.olddata=self.jsonread()
        self.basefile.seek(0)
        self.basefile.truncate()
        self.write(json.dumps(data))
        self.basefile.flush()