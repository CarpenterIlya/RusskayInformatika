for le in range(3): #"M"
    if le == 0:
        file = open("EnglBook.txt", encoding="utf-8")
        put = "ENGL"
    if le == 1:
        file = open("GermBook.txt", encoding="utf-8")
        put = "GERM"
    if le == 3:
        file = open("MathBook.txt", encoding="utf-8")
        put = "MATH"
    if le == 2:
        file = open("PhisBook.txt", encoding="utf-8")
        put = "PHIS"
    if le == 4:
        file = open("tegsBook.txt", encoding="utf-8")
        put = "TEGS"
    ile = file.readlines()
    file.close()
    for i in range(0, len(ile)):
        for ii in range(i + 1, len(ile)):
            if ile[i] == ile[ii]:
                print("Строки", i + 1, "и", ii + 1, "в", put, "и это", ile[i] + "\t","с",ile[ii])
print("Конец")