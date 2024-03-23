import random

def En(count, k_copy, k_necopy, necopy):
    After = []
    Before = []
    podbor(k_necopy, After, Before)
    while True:
        num = random.randint(0, len(After) - 1)
        print(str(count) + ")", After[num])
        otvet = input("Как переводится на англ.? ")
        if not(otvet in []):
            if otvet in ["СТОП", "стоп", "Стоп", "сТОП", "stop", "Stop", "sTOP", "STOP", "CNJG", "cnjg", "Cnjg", "cNJG", "ыещз", "Ыещз", "ыЕЩЗ", "ЫЕЩЗ"]:
                break
            if otvet in Before[num] or otvet + "\n" in Before[num] or otvet + " " + "\n" in Before[num]:
                EnTrue(num, After)
                print("Правильно")
            else:
                EnFalse(num, After, k_copy)
                print("Неправильно! Правильно: ", end="")
                for ii in range(len(Before[num])):
                    print(Before[num][ii], end="")
                    if len(Before[num]) - ii > 2:
                        print(" , ", end="")
                    elif len(Before[num]) - ii == 2:
                        print(" и ", end="")
        else:
            podbor(k_necopy, After, Before)
        print("")
        count += 1

def podbor(k_necopy, After, Before):
    After = []
    Before = []
    a = random.randint(0, len(k_necopy) - 30)
    list = []
    for yyy in range(a, a + random.randint(15, 30)):
        list.append(k_necopy[yyy])
    print(list, a)
    for i in range(0, len(list)):
        After_e, Before_e = (list[i]).split(" - ")
        Before_e = (Before_e).split(" / ")
        After.append(After_e)
        Before.append(Before_e)
def EnTrue(num, After):
    ke = -5
    copy = open("{}Book — копия.txt".format(fora), encoding="utf-8")
    k_copy = copy.readlines()
    copy.close()
    for e in range(len(k_copy)):
        if After[num] + "\n" == k_copy[e] or After[num] == k_copy[e]:
            ke = e
            break
    for mnogo in range(0, len(k_copy) - 1):
        k_copy[mnogo] = k_copy[mnogo + 1]
    k_copy.pop(len(k_copy) - 1)
    if ke != -5:
        for mnogo in range(ke, len(k_copy) - 1):
            k_copy[mnogo] = k_copy[mnogo + 1]
    copy = open("{}Book — копия.txt".format(fora), "w", encoding="utf-8")
    copy.close()
    copy = open("{}Book — копия.txt".format(fora), "a", encoding="utf-8")
    copy.write("Список слов для повторения: \n")
    for E in range(len(k_copy)):
        copy.write(k_copy[E])
    copy.close()

def EnFalse(num, After, k_copy):
    if not(After[num] + "\n" in k_copy):
        copy = open("{}Book — копия.txt".format(fora), "a", encoding="utf-8")
        copy.write("\n" + After[num])
        copy.close()
        print("Добавил", After[num], "В", k_copy)

WHaT = input("Что учим? ")
WHAT = list(WHaT)
count = 1
if WHAT[0] in ["E", "e", "А", "а"]:
    fora = "Engl"
elif WHAT[0] in ["G", "g", "Г", "г"]:
    fora = "Germ"
elif WHAT[0] in ["P", "p", "Ф", "ф"]:
    fora = "Phis"
elif WHAT[0] in ["M", "m", "М", "м"]:
    fora = "Math"
elif WHAT[0] in ["T", "t", "Т", "т"]:
    fora = "tegs"
necopy = open("{}Book.txt".format(fora), encoding="utf-8")
k_necopy = necopy.readlines()
necopy.close()
copy = open("{}Book — копия.txt".format(fora), encoding="utf-8")
k_copy = copy.readlines()
copy.close()
En(count,k_copy, k_necopy, necopy)