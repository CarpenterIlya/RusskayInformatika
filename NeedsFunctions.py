#-----1-----

import math
import matplotlib as plt
import numpy as np
import os
def ReadNamesInFile(): #для чтения имён из файла
    picturePath = "../AnimeBoobas"
    listP = os.listdir(picturePath)
    print(listP)

#-----2-----

def isdecatiinvibor(): # делает число в нужную систему счисления
    number, base = map(float, input("Введите значения числа и систему счисления: ").split())
    abc = list("0123456789abcdefghijklmnopqrstuvwxyz")
    goti = ""
    numbrrr = number
    while numbrrr >= base:
        goti += str(int(numbrrr % base))
        numbrrr //= int(base)
    goti += str(int(numbrrr))
    print(goti)
    ITOG = ""
    for i in range(len(goti) - 1, - 1, - 1):
        ITOG += str(goti[i])
    print(ITOG)

def SmenaSistemSchislenia(): # делает число в нужную систему счисления
    number = int(input("Введите значение числа: "))
    BeforeBase, AfterBase = int(input("Введите системы счисления до и после: "))

    if number % 1 == 0:
        pass
    else:
        pass


    itog = ""
    numbrrr = number
    while numbrrr >= AfterBase:
        itog += str(int(numbrrr % AfterBase))
        numbrrr //= int(AfterBase)
    itog += str(int(numbrrr))
    ITOG = ""
    for i in range(len(itog)-1,-1,-1):
        ITOG += str((int(itog) // (10 ** (len(itog)-i-1)))%10)
    return(ITOG)

def Kol_possle_zap():
    x, e = map(float,input("Введите x и e(кол-во знаков после запятой): ").split())
    GOTOVO = math.exp(x)
    G = GOTOVO
    len_Levo = len(str(GOTOVO // 1)) - 2
    len_Pravo = len(str(GOTOVO)) - len_Levo - 1
    if len_Pravo > e:
        while G % 1 > 0:
            G *= 10
        print(int(G))
        LEVO = str(int(GOTOVO // 1))
        PRAVO = str(int((G % 10 ** len_Pravo) // 10 ** (len_Pravo - e)))
        GOTOVO = LEVO + "." + PRAVO
    else :
        for i in range(len_Pravo, int(e)):
            GOTOVO = str(GOTOVO) + "0"
    print(GOTOVO)

#-----3-----

plohoe = []
names = ["Август","Августин","Авраам","Аврора","Агата","Агафон","Агнесса","Агния","Ада","Аделаида","Аделина","Адонис","Акайо","Акулина","Алан","Алевтина","Александр","Александра","Алексей","Алена","Алина","Алиса","Алла","Алсу","Альберт","Альбина","Альфия","Альфред","Амалия","Амелия","Анастасий","Анастасия","Анатолий","Ангелина","Андрей","Анжела","Анжелика","Анисий","Анна","Антон","Антонина","Анфиса","Аполлинарий","Аполлон","Ариадна","Арина","Аристарх","Аркадий","Арсен","Арсений","Артем","Артемий","Артур","Архип","Ася","Беатрис","Белла","Бенедикт","Берта","Богдан","Божена","Болеслав","Борис","Борислав","Бронислав","Бронислава","Булат","Вадим","Валентин","Валентина","Валерий","Валерия","Ванда","Варвара","Василий","Василиса","Венера","Вениамин","Вера","Вероника","Викентий","Виктор","Виктория","Вилен","Виолетта","Виссарион","Вита","Виталий","Влад","Владимир","Владислав","Владислава","Владлен","Вольдемар","Всеволод","Вячеслав","Габриэлла","Гавриил","Галина","Гарри","Гелла","Геннадий","Генриетта","Георгий","Герман","Гертруда","Глафира","Глеб","Глория","Гордей","Грейс","Грета","Григорий","Гульмира","Давид","Дана","Даниил","Даниэла","Дарина","Дарья","Даяна","Демьян","Денис","Джеймс","Джек","Джессика","Джозеф","Диана","Дина","Динара","Дмитрий","Добрыня","Доминика","Дора","Ева","Евгений","Евгения","Евдоким","Евдокия","Егор","Екатерина","Елена","Елизавета","Елисей","Есения","Ефим","Ефрем","Ефросинья","Жаклин","Жанна","Ждан","Захар","Зинаида","Зиновий","Злата","Зорий","Зоряна","Зоя","Иван","Иветта","Игнатий","Игорь","Изабелла","Изольда","Илга","Илларион","Илона","Илья","Инга","Инесса","Инна","Иннокентий","Иосиф","Ираида","Ираклий","Ирина","Итан","Ия","Казимир","Калерия","Камилла","Камиль","Капитолина","Карина","Каролина","Касьян","Ким","Кир","Кира","Кирилл","Клавдия","Клара","Клариса","Клим","Климент","Кондрат","Константин","Кристина","Ксения","Кузьма,Лада","Лариса","Лев","Леон","Леонид","Леонтий","Леся","Лидия","Лика","Лилиана","Лилия","Лина","Лолита","Луиза","Лукьян","Любовь","Людмила","Магдалина","Майя","Макар","Максим","Марат","Маргарита","Марианна","Марина","Мария","Марк","Марта","Мартин","Марфа","Матвей","Мелания","Мелисса","Милана","Милена","Мирон","Мирослава","Мирра","Митрофан","Михаил","Мия","Модест","Моисей","Мухаммед","Надежда","Назар","Наоми","Наталия","Наталья","Наум","Нелли","Ника","Никанор","Никита","Никифор","Николай","Николь","Никон","Нина","Нинель","Нонна","Нора","Оксана","Олег","Олеся","Оливер","Оливия","Ольга","Оскар","Павел","Парамон","Патрик","Паула","Петр","Платон","Полина","Прасковья","Прохор","Рада","Радмила","Раиса","Райан","Раймонд","Раяна","Регина","Ренат","Рената","Рику","Римма","Ринат","Рита","Роберт","Родион","Роза","Роксана","Роман","Россияна","Ростислав","Руслан","Рустам","Рэн","Сабина","Савва","Савелий","Саки","Сакура","Самсон","Самуил","Сарра","Светлана","Святослав","Севастьян","Семен","Серафима","Сергей","Сильвия","Снежана","Сора","София","Софья","Станислав","Стелла","Степан","Стефания","Таисия","Такеши","Тамара","Тамила","Тарас","Татьяна","Теодор","Тереза","Терентий","Тимофей","Тимур","Тина","Тихон","Томас","Трофим","Ульяна","Урсула","Фаддей","Фаина","Федор","Федот","Феликс","Филат","Филимон","Филипп","Фома","Фрида","Хина","Хлоя","Чарли,","Шейла","Шелли","Эдгар","Эдита","Эдуард","Элеонора","Элина","Элла","Эльвира","Эльдар","Эльза","Эмили","Эмилия","Эмма","Эрик","Эрика","Юи","Юлиан","Юлиана","Юлий","Юлия","Юма","Юна","Юрий","Яков","Ямато","Ян","Яна","Янина"]
Paket_Net = ["Нет","нет","No","no"]
isdecatiinvibor()