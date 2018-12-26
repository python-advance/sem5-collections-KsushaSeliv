import numpy as np
import numpy.random

array = np.random.randint(-50, 50, 10)


#1 Чётные элементы
sortarray1 = []
i = 0
while i < 10:
	if array[i]%2 == 0:
		sortarray1.append(array[i])
	i = i+1
print(sortarray1)
print()

#2 Нечётные элементы

sortarray2 = []
i = 0
while i < 10:
	if array[i]%2 == 1:
		sortarray2.append(array[i])
	i = i+1
print(sortarray2)
print()

#3 Положительные элементы
sortarray3 = []
i = 0
while i < 10:
	if array[i] > 0:
		sortarray3.append(array[i])
	i = i+1
print(list(sortarray3))
print()

#4 Отрицательные элементы
sortarray4 = []
i = 0
while i < 10:
	if array[i] < 0:
		sortarray4.append(array[i])
	i = i+1
print(list(sortarray4))
print()
