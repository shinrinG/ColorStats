import numpy as np
class ResPack:
    _x = 0
    _y = 0
    _h = 0.0
    _s = 0.0
    _v = 0.0
    _l = 0.0
    _a = 0.0
    _b = 0.0

    def __init__(self):
        self._x = 0
        self._y = 0
        self._h = 0.0
        self._s = 0.0
        self._v = 0.0
        self._l = 0.0
        self._a = 0.0
        self._b = 0.0

    def set_xy(self,x,y):
        self._x = x
        self._y = y
    def set_hsv(self,h,s,v):
        self._h = h
        self._s = s
        self._v = v
    def set_lab(self,l,a,b):
        self._l = l
        self._a = a
        self._b = b

    def get_arrays(self):
        
        return np.array([[
            self._x,
            self._y,
            self._h,
            self._s,
            self._v,
            self._l,
            self._a,
            self._b
            ]])