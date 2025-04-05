from oops_classes_objects_instance_attributes_testcase import Rectangle


class MyFirstClass:
    def __init__(self, x,y):
        self.a = x
        self.b = y

    def sum(self):
        return self.a+ self.b

    def multiply(self):
        return self.a * self.b

    r1 = Rectangle()
    r1.method1(10, 20, "red")

    # r1.__init__()

    print(r1.__module__)


    print(r1.color)
    print(r1.h)
    print(r1.w)


# o1 = MyFirstClass(1,2)
# print(o1.a)
# print(o1.sum())
# print(o1.multiply())
#
#
# o2 = MyFirstClass(10,20)
# print(o2.a)
# print(o2.sum())
# print(o2.multiply())
#
# o3 = MyFirstClass(100,200)
# print(o3.a)
# print(o3.sum())
# print(o3.multiply())

