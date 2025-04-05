L = [1, 2, 3, [4,5,[6]], 7, [[[[8]]]]]

# Output = [1,2,3,4,5,6,7,8]

output = []

def flatten_nsted_list(L):
    for e in L:
        # print(e)
        if type(e) == list:
            # print(e)
            flatten_nsted_list(e)
        else:
            output.append(e)

flatten_nsted_list(L)
print(output)

