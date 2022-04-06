import math


class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        if isinstance(re, int) or isinstance(re, float):
            self.re = re
        else:
            raise TypeError
        if isinstance(im, int) or isinstance(im, float):
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        if self.im < 0:
            return f'{self.re}{self.im}i'
        else:
            return f'{self.re}+{self.im}i'
