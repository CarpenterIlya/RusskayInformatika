import math
def CHotCif(Cif):
    return Cif % 2 == 0


def PALINDROP(CHislo):
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
    while


def task1():
    Cif = float(input("Введите число: "))
    print("")


def task2():
    x = float(input("Введите значение x: "))
    a, b = map(float, input("введите интервал [a,b]: ").split())
    if x >= 0:
        print("Fx = ", 2 * (x ** 2 - 5) - x)
    else:
        print("Fx = ", math.tan(x) - 10)
    #
    #
    # Какой график
    #
    #
    print("")


def task3():
    number, base = map(float, input("Введите значения числа и систему счисления: ").split())
    print("Ваше число: ", decimnal_in_new_numeral_system(number, base))
    print("")


def task4():
    x, y = map(float, input("Введите координаты x y: ").split())
    if (y <= x / 1.5 + 3.5 and y >= x / 3 - 1 and y >= x / 2 - 1 and x >= -1) or (y
    = (x ** 2 + 1) ** 0.5 - 1 and x <= -1):
        print("точка находится в левой фигуре")
    elif (False) or (x >= 4 and y <= - 1 and y >= x - 7) or (False) or (x <= 4 and y >= -1 and y <= x - 3) or (
            x <= 4 and y <= 1 and y >= x / 2 + 3):
        print("точка находится в правой фигуре")
    else:
        print("точка находится за фигурами")
    #
    #
    # Доделать!
    #
    #
    print("")


def task5():
    x = float(input("Введите значение x: "))
    if x != 0 and x != 1:
        ne =
        print(" ", max(math.sin(x), math.cos(x), math.log(x)), " ", ne, " ", min(math.sin(x), math.cos(x), math.log(x)))
    else:
        print(" ", max(math.sin(x), math.cos(x), math.log(x)), " ", min(math.sin(x), math.cos(x), math.log(x)))
    print("")


def task6():
    pass


def task7():
    pass


def task8():
    pass


def task9():
    pass


def task10():
    pass
task2()
