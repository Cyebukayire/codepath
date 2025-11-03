# m = [['c', 'a'],['r'] ]
# res = []
# for row in m:
#     res.extend(row)
# print(''.join(res))

# res = [[]]*3
# res[1].append('c')
# print(res)

# Exercise 02
"""
a = 'v'
b = 2.5

print(hash(a)+b)
# print(int(a)+ b)
print('{}{}'.format(a,b))
print(f'{a}{b}')

dct1 = {'hello': 'world!', 'it\'s!': 'me!'}
dct2 = dct1.copy()  ### <- fix this
dct2['it\'s!'] = 'you!'
print(dct1)
print(dct2)

"""

# import numpy as np
# rng = np.random.default_rng(334)
# x1 = rng.random(4)
# x2 = rng.integers(0, 20, size=(5,4))
# x3 = rng.random((5,4,3))
# x4 = rng.integers(0, 10, size=(5,4))

# # print(x2, '\n\n',x4)

# print("Element wise product:\n ",x2 * x4)
# print("Matrix-vector product:\n ", np.dot(x2, x1))

# import numpy as np
# arr = np.array([1,2,3])
# arr = arr.astype(float)
# arr[0] = 1.5  # trying to change 1 to 1.5
# print(arr)
# prints [1,2,3]

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# arr[0] = 10  # Updates the element at index 2 (third element) to 10
# print(arr)

arr = [1, 2, 3, 4, 5]
# print(arr[0::2])
"""
arr[a:b:c] ==> arr[start:stop:step] ==> arr[max(a,0):min(b, len(arr)):]
"""
# when a is < 0: start that many from the end
print(arr[-2:]) # 4, 5
print(arr[2:-1])

# what if 0< a < len(arr)
print(arr[3:]) # 4, 5

# if a == len(arr); 
print( arr[len(arr):]) # []



# what if a > len(arr)
# print(arr[len(arr):1:-1])