class A:
    def __init__(self):
        self.a = 1
    def printA(self):
        print(self.a)

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 2
        super().printA()
        
obj= B()
obj.printA()