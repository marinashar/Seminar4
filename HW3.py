# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random
N = int(input('Введите размер списка: '))
lst = []
for i in range (N):
    lst.append(random.randint(0, 10))
print(lst)
uniqueLst = {}
finalLst = []
for i in lst:
    if uniqueLst.get(i):
        uniqueLst[i] = uniqueLst.get(i) + 1
    else:
        uniqueLst[i] = 1
for j in uniqueLst.items():
    if j[1] == 1:
        finalLst += str(j[0])
print(f'Cписок неповторяющихся элементов исходной последовательности {lst} -> {finalLst}')
