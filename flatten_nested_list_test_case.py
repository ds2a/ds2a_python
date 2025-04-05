L = [1, 2, 3, [4,5,[6]], 7, [[[[8]]]]]

result = []


def flatten_nested_list(L:list):
    for e in L:
        print(e)
        if type(e) == list:
            print("element is list type")
            flatten_nested_list(e)
            # result.extend(e)
        else:
            result.append(e)


flatten_nested_list(L)

print(result)
