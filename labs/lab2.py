import math  # импортировал математику

def CHotCif(Cif):
    if Cif % 2 == 0:
        return "чётное"
    else :
        return "нечётное"

def PALINDROP(CHislo):
    if CHislo / 100 >= 1 and CHislo / 100 < 10:
        if CHislo % 1000 = CHislo % 10:
            CHISLO = "Да"
        else:
        return "Нет"
    else:
        return "Нет"

def decimnal_in_new_numeral_system(number, base):
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return convert(number // base, base) + digits[number % base]

print("Доброе пожаловать в lab2.py")
while True:
    while True:
        SaD = float(input("Введите номер задания (0 - выход): "))  # вводим номер нужного задания
        if SaD % 1 != 0:
            print("Вводи целое число!")  # а вдруг глупый пользователь
        elif SaD > 10:
            print("Такого номера нет!")  # всяко бываетат
        else:
            break
    print("")
    if SaD == 1:  # Надо же как то определить, какое задание ...
        Cif = float(input("Введите число: "))
        #
        #
        # точно ли бесконечный цикл?
        #
        #
        print("a =", (x ** 0.5 - (abs(y)) ** 0.25) / (x - math.log2(y)) ,"b =", math.tan((x - 1) ** 0.5) - (abs(z) ** (1 / 3)) - y ** (1 / 6) + x)
        print("")
    if SaD == 2:
        x = float(input("Введите значение x: "))
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
    if SaD == 3:
        number, base = map(float, input("Введите значения числа и систему счисления: ").split())
        print("Ваше число: ", decimnal_in_new_numeral_system(number, base))
        print("")
    if SaD == 4:
        x, y = map(float,inpit("Введите координаты x y: ").split())
        if (y <= x / 1.5 + 3.5 and y >= x / 3 - 1 and y >= x / 2 -1 and x >= -1) or (y = (x ** 2 + 1) ** 0.5 - 1 and x <= -1):
            print("точка находится в левой фигуре")
        elif (False) or (x >= 4 and y <= - 1 and y >= x - 7) or (False) or (x <= 4 and y >= -1 and y <= x - 3) or (x <= 4 and y <= 1 and y >= x / 2 + 3):
            print("точка находится в правой фигуре")
        else :
            print("точка находится за фигурами")
#
#
#Доделать!
#
#
        print("")
    if SaD == 5:
        x = float(input("Введите значение x: "))
        max = max(math.sin(x), math.cos(x), math.log(x))
        min =
        ne =
        print(" ", max ," ", ne ," ", min)
        print("")
    if SaD == 6:
        
        print("")
    if SaD == 7:
        
        print("")
    if SaD == 8:
        
        print("")
    if SaD == 9:
        part_first, part_second, profit = map(float, input("Введите значения вложений двух предпринимателей и их доход: ").split())
        print("Прибыль первого: ", profit * part_first / (part_first + part_second) ,"Прибыль второго: ", profit * part_second / (part_first + part_second))
        print("")
    if SaD == 0:
        break
