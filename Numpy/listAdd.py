import numpy as np

num1 = [3,45,56,56,67]
num2 = [33,545,66,76,6]

# a = np.array(num1,dtype=int)
b = np.array(num2,dtype=int)

a=  np.random.randint(1,20,5);


#operations on list will be
# Addition
# print(a + b)
# print(a-b)
# print(a * b)
# print(a / b)
# print(a ** b)
# print(a // b)

# print(a)
# print(a.sum)
# print(a.mean)
# print(a.max)
# print(a.argmax)
# print(a.min)
# print(a.argmin)

# print(a > b)
# print(a < b)

# Logical gates 

print(np.logical_and(a,b))
print(np.logical_or(a,b))
print(np.logical_not(a))