class Student_3:
    def __init__(self, name):
        self.name = name

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self,value):
        if 0<=value<=100:
            self._math = value
        else:
            raise ValueError("value must be in [0,100]")

    @math.deleter
    def math(self):
        return self._math

