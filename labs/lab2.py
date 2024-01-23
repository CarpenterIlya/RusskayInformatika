import math
import matplotlib.pyplot as plt
import numpy as np

def CHotCif(Cif):
    return Cif % 2 == 0

def PALINDROP(Cif):
    if CHislo / 100 >= 1 and CHislo / 100 < 10:
        if CHislo % 1000 == CHislo % 10:
            return True
        else:
            return False
    else:
        return False

def decimnal_in_new_numeral_system(number, base):
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return math.convert(number // base, base) + digits[number % base]

def months_to_buy(cost, salary):
    c = 0
    while salary <= cost
	    cost += cost * 0.0315
	    salary += salary * 0.05
	    c += 1
    return c

def fac(i):
    p = 1
    for o in range (1, i):
        p *= o + 1
    return p
        
def task1():
    while True:
        Cif = float(input("Введите число: "))
	if CHotCif(Cif) :
	    print("Чётное")
	else:
	    print("Не чётное")
	if PALISANDROP(Cif):
        	print("Палисандроп")
	else:
        	print("Не палисандроп")

def task2():
    x = float(input("Введите значение x: "))
    a, b = map(float, input("введите интервал [a,b]: ").split())
    fig, ab = plt.subplots()
    ab.set_title("График функции")
    x = np.linspase(a, b, (b - a) * 10)
    if x >= 0:
        print("Fx = ", 2 * (x ** 2 - 5) - x)
	y = 2 * (x ** 2 - 5) - x
    else:
        print("Fx = ", math.tan(x) - 10)
	y = math.tan(x) - 10
    ax.plot(x, y)
    plt.show() #Построение графиков функций в питон it-start - это ссылка

def task3():
    number, base = map(float, input("Введите значения числа и систему счисления: ").split())
    print("Ваше число: ", decimnal_in_new_numeral_system(number, base))

def task4():
    x, y = map(float, input("Введите координаты x y: ").split())
    if (y <= x / 1.5 + 3.5 and y >= x / 3 - 1 and y >= x / 2 - 1 and x >= -1) or (y = (x ** 2 + 1) ** 0.5 - 1 and x <= -1):
        print("точка находится в левой фигуре")
    elif (2 <= (y + 1) ** 2 + (x - 4) ** 2 and x <= 4 and y <= -1) or (x >= 4 and y <= - 1 and y >= x - 7) or (2 <= (y + 1) ** 2 + (x - 4) ** 2 and x >= 4 and y >= -1) or (x <= 4 and y >= -1 and y <= x - 3) or (x <= 4 and y <= 1 and y >= x / 2 + 3):
        print("точка находится в правой фигуре")
    else:
        print("точка находится за фигурами")

def task5():
    x = float(input("Введите значение x: "))
    if x > 0:
        if math.sin(x) > math.cos(x)/x and math.sin(x) > math.log(x):
            if math.cos(x)/x >= math.log(x):
                print(math.sin(x), math.cos(x)/x, math.log(x))
            else:
                print(math.sin(x), math.log(x), math.cos(x)/x)
        elif math.cos(x)/x > math.sin(x) and math.cos(x)/x > math.log(x):
            if math.sin(x) >= math.log(x):
                print(math.cos(x)/x, math.sin(x), math.log(x))
            else:
                print(math.cos(x)/x, math.log(x), math.sin(x))
        else:
            if math.sin(x) >= math.cos(x)/x:
                print(math.log(x), math.sin(x), math.cos(x)/x)
            else:
                print(math.log(x), math.cos(x)/x, math.sin(x))
    elif x < 0:
        if math.sin(x) > math.cos(x)/x:
            print(math.sin(x) , math.cos(x)/x, "log отриц. числа не определено")
        else:
            print(math.cos(x)/x , math.sin(x), "log отриц. числа не определено")
    else:
        print("sin(0) = 0, а log(0) и деление на 0 не определено")


def task6():
    cost, salary = map(float, input("Введите стоимость и зарплату: ").split())
    print(monts_to_buy(cost, salary))

def task8():
    x, e = map(float,input("Введите x и e(кол-во знаков после запятой): ").split())
    GOTOVO = math.exp(x)
    G = GOTOVO
    len_Levo = len(str(G // 1)) - 2
    len_Pravo = len(str(G)) - len_Levo - 1
    LEVO = str(int(GOTOVO // 1))
    if e < 0:
        if -1 * e < len_Levo:
            GOTOVO = int(int(LEVO) // (10 ** (-1 * e)))
        else:
            GOTOVO = " "
    elif len_Pravo > e:
        while G % 1 > 0:
            G *= 10
        PRAVO = str(int((G % 10 ** len_Pravo) // 10 ** (len_Pravo - e)))
        if e == 0:
            GOTOVO = LEVO
        else:
            GOTOVO = LEVO + "." + PRAVO
    else :
        for i in range(len_Pravo, int(e)):
            GOTOVO = str(GOTOVO) + "0"
    print(GOTOVO)
	
def task9():
    ABC = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if i != j:
                ABC += j ** 2
    print(ABC)
    ABC = 0
    for i in range(1, 9):
        abc = 1 ** 3 + 1 ** 2
        for j in range(2, 9):
            abc *= j ** 3 + i ** 2
        ABC += abc
    print(ABC)
    ABC = 0
    for i in range(1, 9):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                ABC += j ** 2 + i - 2 * k
    print(ABC)

def task10():
    pass
    
task2()
