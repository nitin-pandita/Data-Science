import numpy as np

# a = [1,2,4,5,65]

# c = np.array(a);
# print(c)
# print(type(c))


# a = [1,2,4,5,'5',34.54] 

# c = np.array(a ,dtype=str); #we will use dtype to change the data type of the element inside the list
# print(c)


# b = np.ones(3, dtype=int)
# print(b)

# creating 2-d array

# k = np.ones((2,3), dtype=int)

# print(k)


# k = np.empty(4, dtype=int)

# print(k)


# a = [[1,2,3],[4,5,6],[7,8,9]]

# c = np.array(a)

# print(c)

# a = np.zeros(10, dtype=int)
# a[4] = 1
# print(a)

# arange function 
# a = np.arange(1,10,2);
# print(a)

#---------------  line space


# a = np.linspace(2,10,7, dtype=int, endpoint=False)
# print(a) 


# a = np.identity(3, dtype=int)
# print (a)

# b = np.eye(3,4, dtype=int)
# print(b)


# a = np.random.rand(3) * 10
# print(a)

# a = np.random.randint(10,size=(4,4))
# print(a)
# num = np.arange(9,50)
# a = np.array(num)
# print(a)

 
# create identity matrix

# a = np.eye(5,6,dtype=int) # Eye functionality
# print(a)

# cutting the rope
# a = np.linspace(0,5,10)

# for i in range(1, len(a) - 1):
#     print(round(a[i],2))



# a = np.arange(1,8,2,dtype=int)
# print(a)

list_2d = [[1,2,3,56],[56,3,4,5],[6,56,7,8],[78,78,23,2]]
# a = np.array(num1,dtype=int)
a = np.array(list_2d,dtype=int)
# print(list_2d[1][1 : 4])
print(a)
print(a[2 : 4, 1 : 3])



# print(a.data)
# print(a.dtype)
# print(a.shape)
# print(a.strides)

# print(a.data)
# print(a.dtype)
# print(a.shape)
# print(a.strides)
