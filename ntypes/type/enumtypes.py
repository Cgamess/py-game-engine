from collections import *

class EnumList(list):
    def __init__(self, data):
        super().__init__(data)
        
    def __iter__(self):
        return enumerate(self)

class EnumDict(dict):
    def __init__(self, data):
        super().__init__(data)
        
    def __iter__(self):
        return enumerate(self)

class EnumTuple(tuple):
    def __init__(self, data):
        super().__init__(data)
        
    def __iter__(self):
        return enumerate(self)

class EnumDeque(deque):
    def __init__(self, data):
        super().__init__(data)
        
    def __iter__(self):
        return enumerate(self)

class EnumSet(set):
    def __init__(self, data):
        super().__init__(data)
        
    def __iter__(self):
        return enumerate(self)

class EnumCounter(Counter):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        
    def __iter__(self):
        return enumerate(self.items())
    
class EnumDefaultDict(defaultdict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(default_factory, *args, **kwargs)
        
    def __iter__(self):
        return enumerate(self.items())
    
class EnumNamedTuple(namedtuple('EnumNamedTuple', ['x', 'y'])):
    def __new__(cls, x, y):
        return super().__new__(cls, x, y)
    
    def __iter__(self):
        return enumerate(self)
    
class EnumOrderedDict(OrderedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def __iter__(self):
        return enumerate(self.items())
    
class EnumChainMap(ChainMap):
    def __init__(self, *maps):
        super().__init__(*maps)
        
    def __iter__(self):
        return enumerate(self.maps)