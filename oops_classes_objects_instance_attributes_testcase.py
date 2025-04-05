class Rectangle:
    h = None
    w = None
    color = None

    def method1(self, x,y,z):
        self.h = x
        self.w = y
        self.color = z

        print(self.h)
        print(self.w)
        print(self.color)

    def method1(self):
        pass
        

    # print(self.__module__)

    if __name__ == '__main__':
        print("invoked from same script module name")
    else:
        print("invoked from other class")





