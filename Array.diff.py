# Your goal in this kata is to implement a difference function, which subtracts one list from another
# and returns the result.
# array_diff([1,2],[1]) == [2]
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2,2,2,3],[2]) == [1,3]

# def array_diff(a, b):
#     return list(set(a) - set(b))

def array_diff(a, b):
    # res = []
    # for i in a:
    #     if i not in b:
    #         res.append(i)
    # return res
    return [i for i in a if i not in b]

a = [1, 2, 2]
b = [1]

result = array_diff(a, b)
print(result)
