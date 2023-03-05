import numpy as np

a = np.random.randint(1,30,(5,6))

b = a
bool_Arr =b[:, 4] == 24
# print(b) 

b[bool_Arr , 4] = 99

# print(b)
# # print(bool_Arr)

# print(a)
# b = a
# b[bool_Arr, 4] = 99

print(b)

