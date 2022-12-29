# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [2, 1, 78, 4, 2, 56, 7, 1]
list2 = []

for j in range(len(list)):
    key = True
    for i in range(len(list)):
        if j != i:
            if list[i] == list[j]:
                key = False
    if key: list2.append(list[j])

print(list2)