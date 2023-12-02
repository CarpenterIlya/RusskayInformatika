import math  # импортировал математику

def CHotCif(Cif):
    if Cif % 2 == 0:
        CIF = "чётное"
    else :
        CIF = "нечётное"





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
        x, y = map(float, input("Введите значения числителя и знаменателя: ").split())
        print("f(x) = ", (math.cos(math.sin(1 / x ** 2))) ** 2)
        print("")
    if SaD == 4:
        k = float(input("Введите значение k - стороны треугольника: "))
        print("S =", 0.5 * k * (k ** 2 - (0.5 * k) ** 2))
        print("")
    if SaD == 5:
        v1, t1 = map(float, input("Введите значения V1 и T1: ").split())
        v2, t2 = map(float, input("Введите значения V2 и T2: ").split())
        print("V = ", v1 + v2 ,"T = ", ((v1 * t1) + (v2 * t2)) / v1 + v2)  #ВЫДУМАЛ!
        print("")
    if SaD == 6:
        x1, y1 = map(float, input("Введите значения x1 y1: ").split())
        x2, y2 = map(float, input("Введите значения x2 y2: ").split())
        x3, y3 = map(float, input("Введите значения x3 y3: ").split())
        print("R = ", ( ((p - ab)(p - bc)(p - ca)) / p ) ** 0.5)
        print("")
    if SaD == 7:
        A1, B1, C1 = map(float, input("Введите A1, B1, C1: ").split())
        A2, B2, C2 = map(float, input("Введите A2, B2, C2: ").split())
        print("Решение системы = ", A1 * x + B1 * y )
        print("")
    if SaD == 8:
        V1, V2, S1, T = map(float, input("Введите значения V1, V2, S1 и T, через пробел: ").split())
        while True:
            if V1 < 1 or V1 > 100 or V2 < 1 or V2 > 100 or S1 < 1 or S1 > 100 or T < 1 or T > 100
                print("Каждое из значений лежит от 1 до 100 включительно!")
            else:
                break
        print("S = ", S1 + V1 * T + V2 * T)
        print("")
    if SaD == 9:
        part_first, part_second, profit = map(float, input("Введите значения вложений двух предпринимателей и их доход: ").split())
        print("Прибыль первого: ", profit * part_first / (part_first + part_second) ,"Прибыль второго: ", profit * part_second / (part_first + part_second))
        print("")
    if SaD == 0:
        break
