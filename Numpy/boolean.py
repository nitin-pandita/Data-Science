import numpy as np

a = np.array([45,45,65,67,45,45,45,23])
b = np.array(['a','b','c','d','e','f','k','i'])

new_arr1 = a[a > 10]
# print(new_arr1)
# new_arr = a[(a > 10) & (a < 200)]

# print(new_arr)

print(a)
print(b)
ind = np.where(a == 45)

print(ind)
print(b[ind])