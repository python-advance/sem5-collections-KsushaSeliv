import random
import numpy as np

array = np.random.randint(0, 100, 10)
print(array)  

array1 = list(filter(lambda x: not x%2, array))
array2 = list(filter(lambda x: x%2, array))

print(array1)
print(array2)
