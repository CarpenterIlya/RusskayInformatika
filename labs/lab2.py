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
    c = 0
    while salary <= cost
	    cost += cost * 0.0315
	    salary += salary * 0.05
	    c += 1
    return c


def fac(i):
    for o in range (1, i):
        p *= o + 1
        
def task1():
    while True:
        Cif = float(input("Введите число: "))
	if CHotCif :
	    print("Чётное")
	else:
	    print("Не чётное")
	if PALISANDROP:
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
    if (y <= x / 1.5 + 3.5 and y >= x / 3 - 1 and y >= x / 2 - 1 and x >= -1) or (y
    = (x ** 2 + 1) ** 0.5 - 1 and x <= -1):
        print("точка находится в левой фигуре")
    elif (False) or (x >= 4 and y <= - 1 and y >= x - 7) or (False) or (x <= 4 and y >= -1 and y <= x - 3) or (
            x <= 4 and y <= 1 and y >= x / 2 + 3):
        print("точка находится в правой фигуре")
    else:
        print("точка находится за фигурами")

def task5():
    x = float(input("Введите значение x: "))
    if x != 0 and x != 1:
        ne =
        print(" ", max(math.sin(x), math.cos(x), math.log(x)), " ", ne, " ", min(math.sin(x), math.cos(x), math.log(x)))
    else:
        print(" ", max(math.sin(x), math.cos(x), math.log(x)), " ", min(math.sin(x), math.cos(x), math.log(x)))

def task6():
    cost, salary = map(float, input("Введите стоимость и зарплату: ").split())
    print(monts_to_buy(cost, salary))

def task8():
    x = int(input("Введите x: "))
    p = 1
    a = 0
    for i in range (1, 5):
        a += (x ** i)/fac(i)
    print(a)

def task9():
    ABC = 0
    for i in range(9):
        for j in range(9):
            if i != j:
                ABC += j ** 2
    print(ABC)

def task10():
    pass
    
task2()
