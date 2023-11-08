import math                                         #импортировал математику
while True:
    while True:
        SaD = float(input("Введите номер задания: "))     #вводим номер нужного задания
        if SaD // 1 != 0:
            print("Вводи целое число!")                    #а вдруг глупый пользователь
        elif SaD > 9 :
            print("Такого номера нет!")                     #всяко бывает
        else :
            break
    print("")
    if SaD == 1:                                    #Надо же как то определить, какое задание ...
        x, y, z = map(float,input("Введите значения x y z соответственно: ").split())            #вводим
        print("a =", ((abs(x - 1)) ** (1 / 3) + math.cos(y))/(math.tan(y) + math.sin(y)))      #вычислил и ввёл
        print("b =", (math.log((abs(z - 1)) ** 0.5)) + (abs(y) ** (1/3)/((1 + z ** 2) ** 0.5) + math.sin(y) * math.sin(x))                              #вычислил и ввёл
    if SaD == 2:
        x = float(input("Введите значение x: "))                                          #вводим
        print("f(x) = ", ((x ** 2 + 2 * x) / b - 1 * x ** 2) ** 0.5)                         #вычислил и ввёл

    if SaD == 3:
        x = float(input("Введите значение x: "))                                            #вводим
        print("f(x) = ", (math.tan(x)) ** 2 * abs(math.log(x ** 2)))                         #вычислил и ввёл
                                                                           #для эстетичности
    if SaD == 4:
        x1 , y1 = map(float,input("Введите координаты первой точки (x, y): ").split())            #вводим
        x2 , y2 = map(float,input("Введите координаты второй точки: ").split())                    #вводим
        x3 , y3 = map(float,input("Введите координаты третьей точки: ").split())                    #вводим
        AB = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        BC = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        AC = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5                                            #вычислил длины сторон
        if AB == BC :
            h = (AB ** 2 - (AC / 2) ** 2) ** 0.5
            print("S =", h * AC )
        elif BC == AC :
            h = (BC ** 2 - (AB / 2) ** 2) ** 0.5
            print("S =", h * AB )
        elif AC == AB :
            h = (AC ** 2 - (BC / 2) ** 2) ** 0.5
            print("S =", h * BC )
        else:
            h = (AB ** 2 - (AC / 2) ** 2) ** 0.5
            print("S =", h * AC )
        print("P =", (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 + ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5) * 2)
        print("")
    if SaD == 5:
        m1 , m2 = map(float,input("Введите массы двух тел: ").split())             #вводим
        r = float(input("Введите расстояние между телами: "))                #вводим
        print("F = ", G * m1 * m2 / r)

    if SaD == 6:
        print("")
    exit = float(input("введите 1 для выхода: "))
    if exit == 1:
        break
