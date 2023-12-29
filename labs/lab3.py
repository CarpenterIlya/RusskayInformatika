def print_char_list(array):
    pass
def proverka1(array, symbol):
    pass
def proverka2(array, first_symbol, second_symbol):
    pass
def proverka3(array):
    pass
def proverka4(array):
    pass
def proverka5(array):
    pass
def print_char_2d_array(array):
    pass
def vistrel(row, column, array):
    pass
def task_1():
    pass
def task_2():
    a = int(input("Введите размер стороны поля для игры Морской бой: "))
    mas = [["."] * a for i in range (a)]

def task_3():
    with open('DLYA_task_3.txt', 'w+') as f:
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
def task_8():
    pass

task_3()
