import numpy as np

# num = [1,2,0,0,4,0]

# a = np.array(num, dtype=int)

# new_arr = np.where(a  > 0)

# print(*new_arr[0])


# a = np.arange(1,20,2)

# new_arr = np.where(a % 3 == 0)
# print(a)
# print(*new_arr[0])

# a = np.arange(1,11)
# print(a)

# a[a % 2 != 0] = -1
 

# print(a)

# a = np.array([11,2,13,4,15,6,27,8,19])


# a[a.argmax()] = 0 # argmax is just returning the index of the max element

# print(a) # at last just returning 'a'


a = np.arange(1,11,dtype=int)
# the range is from 3 : 9, and we have to make all the element in between negative

a[2:8] = np.multiply(a[2:8],-1)
 
print(a)
