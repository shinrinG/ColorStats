class Rect:
    _x=0
    _y=0
    _w=0
    _h=0
    def __init__(self,x,y,w,h):
        self._x=x
        self._y=y
        self._w=w
        self._h=h

    def pos_LU(self):
        return self._x,self._y 
    def pos_RB(self):
        return (self._x + self._w),(self._y + self._h) 