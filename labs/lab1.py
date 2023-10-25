import math                                         #импортировал математику
while True:
    SAD = int(input("Введите номер задания: "))     #вводим номер нужного задания
    print()
    if SAD == 1:                                    #Надо же как то определить, какое задание ...
        x, y, z = map(float,input("Введите значения x y z соответственно: ").split())
        print("a =", ((abs(x - 1)) ** (1 / 3) + math.cos(y))/(math.tan(y) + math.sin(y)))      #вычислил и ввёл
        print("b =", (math.log((abs(z - 1)) ** 0.5)) + (abs(y) ** (1/3)/((1 + z ** 2) ** 0.5) + math.sin(y) * math.sin(x))                              #вычислил и ввёл
        print()
    elif SAD == 2:
        x = float(input("Введите значение x: "))
        print("f(x) = ", ((x ** 2 + 2 * x) / b - 1 * x ** 2) ** 0.5)                          #вычислил и ввёл
        print()
    elif SAD == 3:
        x = float(input("Введите значение x: "))
        print("f(x) = ", (math.tan(x)) ** 2 * abs(math.log(x ** 2)))                          #вычислил и ввёл
        print()                                                                               #для эстетичности
    elif SAD == 4:
        x1 , y1 = map(float,input("Введите координаты первой точки (x, y): ").split())
        x2 , y2 = map(float,input("Введите координаты второй точки: ").split())
        x3 , y3 = map(float,input("Введите координаты третьей точки: ").split())
        print("S =", () * 2)
        print("P =", (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 + ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5) * 2)
    elif SAD == 5:
        V_1 , T_1 = map(float,input("Введите зачения объёма(м^3) и температы(Градусы) первого куска воды: ").split())
        V_2 , T_2 = map(float,input("Введите зачения объёма(м^3) и температы(Градусы) второго куска воды: ").split())
        print()
        print()
    exit = float(input("введите 1 для выхода: "))
    if exit == 1:
        break
