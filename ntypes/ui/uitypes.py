import pygame as pg
from collections import deque

class uiobjects:
    def __init__(self, pygame : pg) -> None:
        self.objectlist : deque = deque([])
    def new(self, pygame : pg, xy : tuple, objtype : int = 0):
        self.objectlist.append(object(pg, xy, objtype))

class uiobject:
    def __init__(self, pygame : pg, xy : tuple, objtype : int = 0) -> None:
        self.objtype=objtype
        self.xy=xy
        