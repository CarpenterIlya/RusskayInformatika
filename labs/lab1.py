import math  # импортировал математику
while True:
    while True:
        print("")
        SaD = float(input("Введите номер задания (0 - выход): "))  # вводим номер нужного задания
        if SaD % 1 != 0:
            print("Вводи целое число!")  # а вдруг глупый пользователь
        elif SaD > 9:
            print("Такого номера нет!")  # всяко бываетат
        else:
            break
    if SaD == 0:
        break
    if SaD == 1:  # Надо же как то определить, какое задание ...
        x, y, z = map(float, input("Введите значения x y (y != 2) z: ").split())
        print("a =", (x ** 0.5 - (abs(y)) ** 0.25) / (x - math.log2(y)),"b =", math.tan((x - 1) ** 0.5) - (abs(z) ** (1 / 3)) - y ** (1 / 6) + x)
        print("")
    if SaD == 2:
        x = float(input("Введите значение x: "))
        print("f(x) = ", x ** 2 + (-5 * x) ** 0.5 / (2 * x + 5))
        print("")
    if SaD == 3:
        x = float(input("Введите значение x: "))
        print("f(x) = ", (math.cos(math.sin(1 / x ** 2))) ** 2)
        print("")
    if SaD == 4:
        k = float(input("Введите значение k - стороны треугольника: "))
        print("S =", 0.5 * k * (k ** 2 - (0.5 * k) ** 2))
        print("")
    if SaD == 5:
        v1, t1 = map(float, input("Введите значения Объёма(V1) и Температуры(T1): ").split())
        v2, t2 = map(float, input("Введите значения V2 и T2: ").split())
        print("V = ", v1 + v2 ,"T = ", ((v1 * t1) + (v2 * t2)) / (v1 + v2))  #ВЫДУМАЛ!
        print("")
    if SaD == 6:
        print("Дан треугольник с вписанной окружностью")
        x1, y1 = map(float, input("Введите значения x1 y1: ").split())
        x2, y2 = map(float, input("Введите значения x2 y2: ").split())
        x3, y3 = map(float, input("Введите значения x3 y3: ").split())
        ab = ((x2 - x1) ** 2 + (y2 + y1) ** 2) ** 0.5
        bc = ((x3 - x2) ** 2 + (y3 + y2) ** 2) ** 0.5
        ca = ((x1 - x3) ** 2 + (y1 + y3) ** 2) ** 0.5
        p = (ab + bc + ca) / 2
        print("R = ", ( ((p - ab)(p - bc)(p - ca)) / p ) ** 0.5)
        print("")
    if SaD == 7:
        A1, B1, C1 = map(float, input("Введите значения A1 B1 C1: ").split())
        A2, B2, C2 = map(float, input("Введите значения A2 B2 C2: ").split())
        print("X = ",(C1 * B2 - C2 * B1) / (A1 * B2 + A2 * B1), "Y =", (A1 * C2 - A2 * C1) / (A1 * B2 + A2 * B1))
    if SaD == 8:
        V1, V2, S1, T = map(float, input("Введите значения V1 V2 S1 и T: ").split())
        print("S = ", V1 * T + V2 * T + S1)
    if SaD == 9:
        part_first, part_second, profit = map(float, input("Введите значения вложений двух предпринимателей и их доход: ").split())
        print("Прибыль первого: ", profit * part_first / (part_first + part_second), "Прибыль второго: ",profit * part_second / (part_first + part_second))
        print("")
