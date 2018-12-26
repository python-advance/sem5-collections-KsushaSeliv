import numpy as np
import numpy.random

#1 Функции языка
array = np.random.randint(0, 100, 10)
print(array)
print()

sortarray0 = array
sortarray0.sort()
print(sortarray0)
print()

sortarray1 = sorted(array)
print(sortarray1)
print()

sortarray2 = sorted(array, reverse = True)
print(sortarray2)
print()

#2 Вставка
def sortarray3(array):
	for i in range(len(array) - 1):
		j = i - 1 
		key = array[i]
		while array[j] > key and j >= 0:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array
print(sortarray3(array))
print()

#3 Плавная
def sortarray4(array):
    def downHeap(array, k, n):
        new_elem = array[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and array[child] < array[child+1]:
                child += 1
            if new_elem >= array[child]:
                break
            array[k] = array[child]
            k = child
        array[k] = new_elem
  
    size = len(array)
    for i in range(size//2-1,-1,-1):
        downHeap(array, i, size)
    for i in range(size-1,0,-1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        downHeap(array, 0, i)
    return array

print(sortarray4(array))
print()


![alt](https://github.com/python-advance/sem5-collections-KsushaSeliv/blob/master/invar/2.JPG)
