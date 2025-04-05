import copy

original_list = [[1, 2], [3, 4]]

assignment_operator_list = original_list
assignment_operator_list.append([7,8])

print(original_list)
print(assignment_operator_list)

print("original :: ", id(original_list))

for e in original_list:
    print(id(e))
shallow_copy_object = original_list[:]

shallow_copy_object.append([5,6])

#modification the object level is not getting reflected to original object
print(original_list)
print(shallow_copy_object)

shallow_copy_object[0].append(9)
print(original_list)
print(shallow_copy_object)


print("shallow_copy :: ", id(shallow_copy_object))
for e in shallow_copy_object:
    print(id(e))


deep_copy_object = copy.deepcopy(original_list)

print("deep copy :: ", id(deep_copy_object))
for e in deep_copy_object:
    print(id(e))


