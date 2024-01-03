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
    pass
def task_5():
    stop = input("Введите стоп слово: ")
    while True:
        U = input("Введите текст: ")
        u = U[0]
        if U == stop:
            break
        elif ord(u) in [1030, 1064]:
            U = open("DLYA_task_5-1.txt", "w")
        else:
            U = open("DLYA_task_5-2.txt", "w")
    U.close()

def task_6():
    pass
def task_7():
    pass

task_3()
