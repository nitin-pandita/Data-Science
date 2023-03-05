import numpy as np

# same dimensions
# a = np.random.randint(1,10,(3,3));
# b = np.random.randint(1,10,(3,3));


# Different Dimensions

# a = np.random.randint(1,10,(3,3))

# b = np.random.randint(1,10, (3))

# print(b)

# same dimensions but different row and col

a = np.random.randint(1,10,(2,3));
b = np.random.randint(1,10,(3,2));

# print(a,b)

# for this we can simply transpose the array
b = np.transpose(b)


output = a - b


print(output)