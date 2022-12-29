# ДОП. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


fileName1 = '1.txt' # важно соблюдать синтаксис вида: 15*x^3 + x^2 - 4*x - 1 = 0 (пробелы вокруг каждого +/-)
fileName2 = '2.txt' # важно соблюдать синтаксис вида: - x^2 + 7 = 0 (пробелы вокруг каждого +/-)
fileResult = 'result_1-2.txt'

count = 0

def fileOpen(fileName):
    with open(fileName, 'r') as file:
        for line in file:
            return line.split()

def fileRes(fileName, dict):

    for i in range(count, -1, -1): # удаляем нули
        if dict[i] == 0: dict.pop(i)

    txt = ''
    for i in range(count, -1, -1):
        if i in dict:
            if i == 0: 
                if dict[i] < 0:
                    txt += f'- {abs(dict[i])}'
                else:
                    txt += f'+ {dict[i]}'
            elif i ==1:
                if dict[i] < 0:
                    txt += f'- {abs(dict[i])}*x '
                else:
                    txt += f'+ {dict[i]}*x '
            else:
                if dict[i] < 0:
                    txt += f'- {abs(dict[i])}*x^{i} '
                else:
                    txt += f'+ {dict[i]}*x^{i} '

    if txt[0] == '+': txt = txt[2:]
    
    with open(fileName, 'w') as file:
        file.write(f'{txt}') 
    
    return txt

def transf(fileName): # трансформируем строку в словарь, где ключ - степень, значение - коэффициент
    
    global count
    mn = fileOpen(fileName)

    i = 0
    dictionMn = {}
    while mn[i] != '=':
        if len(mn[i]) >= 3: # формат 4*x, 2*x^2 и т.д.
            if mn[i][-1] == 'x': 
                dictionMn[1] = int(mn[i][0:-2])
            else:
                if mn[i][0].isdigit():
                    if int(mn[i][-1]) > count: count = int(mn[i][-1])
                    dictionMn[int(mn[i][-1])] = int(mn[i][0:-4])
                else:
                    if len(mn[i]) == 3:
                        dictionMn[int(mn[i][-1])] = 1
                    else:
                        dictionMn[int(mn[i][-1])] = int(mn[i][0:-4])
        
        if len(mn[i]) == 1 and mn[i].isdigit(): 
            dictionMn[0] = int(mn[i])
        i += 1

    i = 0
    while mn[i] != '=': # прописываем минусы
        if mn[i] == '-': 
            if len(mn[i+1]) > 3:
                dictionMn[int(mn[i+1][-1])] = -dictionMn[int(mn[i+1][-1])]
            elif len(mn[i+1]) == 3:
                if mn[i+1][0].isdigit():
                    dictionMn[1] = -dictionMn[1]
                else:   
                    dictionMn[int(mn[i+1][-1])] = -1
            elif len(mn[i+1]) == 1:
                dictionMn[0] = -dictionMn[0]
            
        i += 1
    return dictionMn

def sumDict(dict1, dict2):
    dictRes = {}
    for i in range(count, -1, -1):
        if i in dict1 and i in dict2:
            dictRes[i] = dict1[i] + dict2[i]
        elif i in dict1:
            dictRes[i] = dict1[i]
        elif i in dict2:
            dictRes[i] = dict2[i]
    return dictRes

dict1 = transf(fileName1)
dict2 = transf(fileName2)
dictRes = sumDict(dict1, dict2)

print(f'Сумма многочленов: {fileRes(fileResult, dictRes)}')

