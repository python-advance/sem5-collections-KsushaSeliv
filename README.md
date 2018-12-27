# sem5-collections
<h1>Инвариатное задание</h1>
4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

```python
import numpy as np # это библиотека языка Python, добавляющая поддержку больших многомерных массивов и матриц, вместе с большой библиотекой высокоуровневых (и очень быстрых) математических функций для операций с этими массивами.
import numpy.random #Для создания массивов со случайными элементами служит модуль numpy.random

#1 Функции языка
array = np.random.randint(0, 100, 10) 
print(array)

array1 = sorted(array) #встроенная функции sorted() принимает итерируемый тип и возвращает отсортированный список
print(array1)

array2 = sorted(array, reverse = True) #захотим перевернём, не захотим - не перевернём
print(array2)

#2 Вставка
def array3(array):
	for i in range(len(array) - 1):
		j = i - 1 
		key = array[i]
		while array[j] > key and j >= 0:
			array[j + 1] = array[j]
			j = j- 1
		array[j + 1] = key
	return array
print(array3(array))

#3 Плавная
def array4(array):
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

print(array4(array))
```

![alt](https://github.com/python-advance/sem5-collections-KsushaSeliv/blob/master/invar/17.JPG)

4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

```python
import numpy as np # это библиотека языка Python, добавляющая поддержку больших многомерных массивов и матриц, вместе с большой библиотекой высокоуровневых (и очень быстрых) математических функций для операций с этими массивами.
import numpy.random #Для создания массивов со случайными элементами служит модуль numpy.random

array = np.random.randint(-30, 100, 10)
print(array)

#1 Чётные элементы
array1 = []
i = 0
while i < 10:
	if array[i]%2 == 0: #пока остаток от деления на два = 0, записываем в массив
		array1.append(array[i])
	i = i+1
print(array1)

#2 Нечётные элементы
array2 = []
i = 0
while i < 10:
	if array[i]%2 == 1:  #пока остаток от деления на два = 1, записываем в массив
		array2.append(array[i])
	i = i+1
print(array2)

#3 Положительные элементы
array3 = []
i = 0
while i < 10:
	if array[i] > 0: #пока элемент больше нуля записываем в массив
		array3.append(array[i])
	i = i+1
print(array3)

#4 Отрицательные элементы
array4 = []
i = 0
while i < 10:
	if array[i] < 0: #пока элемент меньше нуля записываем в массив
		array4.append(array[i])
	i = i+1
print(array4)
```

![alt](https://github.com/python-advance/sem5-collections-KsushaSeliv/blob/master/invar/18.JPG)

<h1>Вариативное задание</h1>
Создание программы по разделению одного словаря на произвольное количество словарей по определенному критерию, задаваемому в виде лямбда функции.

```python
import numpy as np
import random

array = np.random.randint(0, 50, 10) #его будем делить на два
print(array)  

array1 = list(filter(lambda x: not x%2, array)) #сюда запихнём те элементы, которые делятся на два без остатка
array2 = list(filter(lambda x: x%2, array)) #соответсвенно, сюда наоборот

print(array1)
print(array2)
```
![alt](https://github.com/python-advance/sem5-collections-KsushaSeliv/blob/master/var/19.JPG)











