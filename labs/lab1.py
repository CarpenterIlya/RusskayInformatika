import math #импортировал математику
while True:
    SAD = int(input("Введите номер задания: ")) #вводим номер нужного задания
    print()
    if SAD == 1: #Надо же как то определить, какое задание ...
        x, y, z = map(float,input("Введите x y z соответственно: ").split())
        print("a =", (x ** 0.5 - (abs(y)) ** 0.25)/(x - math.log2(y)))   #вычислил и ввёл
        print("b =", math.tan((x - 1) ** 0.5) - (abs(z)) ** (1 / 3) - y ** (1 / 6) + x)  #вычислил и ввёл
        print()
    elif SAD == 2:
        x = float(input("Введите значение x: "))
        print("f(x) = ", x ** 2 + (-5 * x) ** 0.5 / (2 * x + 5)) #вычислил и ввёл
        print()
    elif SAD == 3:
        x = float(input("Введите значение x: "))
        print("f(x) = ", (math.cos(math.sin(1 / x ** 2))) ** 2)   #вычислил и ввёл
        print() #для эстетичности
    elif SAD == 4:
        k , A , B = map(float,input("Введите k A B (A и B в градусах), в соответствующем порядке: ").split())
        print("S =", k ** 2 * (math.sin(A) * math.sin(B)) / (2 * math.sin(A + B))
    exit = float(input("введите 1 для выхода: "))
    if exit == 1:
        break
