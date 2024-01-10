def print_char_list(array):
    for i in range(len(array)):
        print(array[i])

def proverka1(array, symbol):
    count = 0
    for i in range(len(array)):
        if array[i] == symbol:
            count += 1
    return count > 0

def proverka2(array, first_symbol, second_symbol):
    count = 0
    if len(array) <= 1:
        print("Невозможно подобрать пары!")
    else:
        for i in range(len(array)-1):
            if (array[i] == str(first_symbol) and array[i+1] == str(second_symbol)) or (array[i+1] == str(first_symbol) and array[i] == str(second_symbol)):
                count += 1
        if (array[0] == str(first_symbol) and array[len(array)-1] == str(second_symbol)) or (array[len(array)-1] == str(first_symbol) and array[0] == str(second_symbol)):
            count += 1
        print("Число пар через числа (включая пер. и пос.) =", count)

def proverka3(array):
    count = 0
    if len(array) <= 1:
        print("Невозможно подобрать пары!")
    for i in range(len(array)-1):
        if array[i] == array[i+1] :
            if array[i] == array[i+1]:
                count += 1
    if array[0] == array[len(array)-1]:
        count += 1
    print("Число пар (включая пер. и пос.) =", count)
    
def proverka4(array):
    count = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[i] == array[i+1] and array[j] == array[j+1]:
                count += 1
    if count > 0:
        print("Две пары одинаковых символов есть!")

def proverka5(array):
    print("Кол-во пробелов =", array.count(" "))
def print_char_2d_array(array):
    pass
def vistrel(row, column, array):
    pass
def task_1():
    array = input("Введите массив: ")
    array = array.split()
    symbol = input("Введите symbol: ")
    if proverka1(array, symbol):
        print("symbol есть в array!")
    else:
        print("symbol нет в array!")
    first_symbol, second_symbol = map(int,input("Введите пару символов: ").split())
    proverka2(array, first_symbol, second_symbol)
    proverka3(array)
    proverka4(array)
    proverka5(array)
def task_2():
    a = int(input("Введите размер стороны поля для игры Морской бой: "))
    mas = [["."] * a for i in range (a)]

def task_3():
    with open('DLYA_task_3.txt', 'a') as f:
        for i in range(5):
            print("Введите текст: ")
            f.write(input())
    
def task_4():
    array = input("Введите что-то: ")
    array = array.split()
    c = 0
    while True:
        for i in range(len(array)-2):
            c += 1
            if len(array[i] + array[i+1]) < 10:
                c = 0
                array[i] = array[i] + array[i+1]
                if i <= len(array) - 1:
                    for g in range(i, len(array)-1):
                        array[g] = array[g + 1]
                array.pop(len(array)-1)
        if c >= len(array):
            break
    number = int(input("Введите номер строки для отметки: "))
    otmetka(array, number)
    print_string_list(array)
#
#
# Не работает
#
#
def sraw(u):
    return ((ord(u) >= 1040 and ord(u) < 1072) or (ord(u) >= 65 and ord(u) < 91))

def task_5():
    stop = input("Введите стоп слово: ")
    while True:
        text = input("Введите текст: ")
        u = text[0]
        if text == stop:
            break
        elif sraw(u):
            file = open("DLYA_task_5-1.txt", "w+", encoding="utf-8")
            file.write(text)
            file.close()
        else:
            file = open("DLYA_task_5-2.txt", "w+", encoding="utf-8")
            file.write(text)
            file.close()

def task_6():
    pass

def proverka1(SP, G):
    count = 0
    for i in range(len(SP)):
        if SP[i] == SP[G]:
            count += 1
    return count > 0
    
def task_7():
    RAS = input("Вводи: ")
    RAS = RAS.split()
    a = int(input("Сколько хотите названий? "))
    SP = []
    g = 0
    while g < a: # создание переменных
        name = ""
        i = int(random.randint(1, 20)) # количество букавак
        for I in range(i-1):
            name += chr(random.randint(1040, 1104) or random.randint(65, 91) or random.randint(97, 123))
        G = g
        SP[g] = name + "." + RAS[random.randint(0, len(RAS)-1)]
        if proverka1(SP, G):
            g -= 1
        else:
            print(SP[g])
        g += 1

task_3()
