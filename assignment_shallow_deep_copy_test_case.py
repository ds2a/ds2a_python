import copy

a = "deepak"
b = 1, 2, 3, 4    #or b = (1, 2, 3, 4)  or b = tuple(1,2,3,4)
c = [1, 2, 3, 4]
d = {1: 10, 2: 20, 3: 30}

#shallow copy
a1 = copy.copy(a)
b1 = copy.copy(b)
c1 = copy.copy(c)
d1 = copy.copy(d)

print("immutable - id(a)==id(a1)", id(a) == id(a1))
print("immutable - id(b)==id(b1)", id(b) == id(b1))
print("mutable - id(c)==id(c1)", id(c) == id(c1))
print("mutable - id(d)==id(d1)", id(d) == id(d1))

# immutable - id(a)==id(a1) True
# immutable - id(b)==id(b1) True
# mutable - id(c)==id(c1) False
# mutable - id(d)==id(d1) False
# If I perform deepcopy:

a2 = copy.deepcopy(a)
b2 = copy.deepcopy(b)
c2 = copy.deepcopy(c)
d2 = copy.deepcopy(d)

print("immutable - id(a)==id(a1)", id(a) == id(a2))
print("immutable - id(b)==id(b1)", id(b) == id(b2))
print("mutable - id(c)==id(c1)", id(c) == id(c2))
print("mutable - id(d)==id(d1)", id(d) == id(d2))
# results are the same:
#
# immutable - id(a)==id(a1) True
# immutable - id(b)==id(b1) True
# mutable - id(c)==id(c1) False
# mutable - id(d)==id(d1) False
# If I work on assignment operations:

a3 = a
b3 = b
c3 = c
d3 = d


# then results are:
#
# immutable - id(a)==id(a1) True
# immutable - id(b)==id(b1) True
# mutable - id(c)==id(c1) True
# mutable - id(d)==id(d1) True
