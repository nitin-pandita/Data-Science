import numpy as np

a = np.arange(24).reshape(4,6)


b  = a

bool_Arr = b[: ,4] > 10

b[bool_Arr,4] = 99

print(b)