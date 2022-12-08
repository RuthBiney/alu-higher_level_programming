#!/usr/bin/python3
"""the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defining the square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """representing of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)
    
    def update(self, *args, **kwargs):
        """update"""
        if args:
            for r, u in enumerate(args):
                if r == 0:
                    self.id = u
                elif r == 1:
                    self.size = u
                elif r == 2:
                    self.x = u
                else:
                    self.y = u
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

     def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d







