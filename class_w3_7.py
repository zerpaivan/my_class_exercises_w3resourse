#  Write a Python class to implement pow(x, n)
class Script_7():
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def pow_x(self):
        p = self.x ** self.n
        return p


op = Script_7(2, 3)
print(op.pow_x())
