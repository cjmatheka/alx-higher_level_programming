#!/usr/bin/python3

"""
Inherits from Rectangle class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of square instance
        return: square instance string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
