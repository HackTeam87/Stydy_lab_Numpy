#-*- coding: utf-8 -*-
#! /usr/bin/python3
import numpy as np

print('''\n 1. Створіть масив зі списку, що складається з чисел від 0 до 9, за допомогою
функції array (Install)) з модуля numpy.''')
arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr1)



print('''\n 2. Створіть масив, що складається з непарних чисел від 1 до 19, за допомогою
функції arange (Install)) з модуля NumPy.''')
# print(arr1[arr1 %2 == 1])
arr2 = np.arange(1,20,2)
print(arr2)

print('\n 3. Створіть масив, що складається з двадцяти нулів.')
arr3 = np.zeros((1, 20 ))
print(arr3)

print('''\n 4. Створіть двовимірний масив, що складається з двадцяти одиниць, в якому 5
рядків і 4 стобці.''')
arr4 = np.ones([4, 5, 1],dtype='int')
print(arr4)


print('''\n 5. Створіть масив, що складається з п'яти рівномірно розподілених чисел від 3 до 7.''')
arr5 = np.linspace(3,7,5,dtype='int')
print(arr5)


print('''\n 6. Створіть двовимірний масив, що складається з 9 рівномірно розподілених чисел від 3 до 7.''')
arr6 = np.linspace(start=[3], stop=[7], num=9 , dtype='float32')
print(arr6)




print('''
\n 7. Створіть масив, що складається з 10 випадкових цілих чисел з діапазону від 1 до 100, 
надайте його максимальне значення змінної max_number і виведіть
значення цієї змінної за допомогою функції print (Install)).
 ''')
arr7 = np.random.randint(1,100,10)
print(arr7)
max_number = np.amax(arr7)
print('max_number= ' + str(max_number))