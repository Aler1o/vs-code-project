def pz1():
    file = open("pz1in.txt", encoding="utf-8")
    inStr = file.read()
    print(inStr)

    fileOut = open("pz1out.txt", 'w', encoding='utf-8')
    fileOut.write(inStr)


def pz2():
    filein = open("pz2in.txt", encoding="utf-8")
    listIn = filein.readlines()
    print(listIn)

    fileOut = open("pz2out.txt", 'w', encoding='utf-8')
    for row in listIn:
        fileOut.write(row)


def pz3():
    filein = open("pz3in.txt", encoding="utf-8")
    listIn = filein.readlines()

    listIn.reverse()
    print(listIn)

    fileOut = open("pz3out.txt", 'w', encoding='utf-8')
    for row in listIn:
        fileOut.write(row)

def pz4():
    filein = open("pz4in.txt", encoding="utf-8")
    listIn = filein.readlines()
    indexOut = 0
    for row in listIn:
        for s in row:
            if s == ',':
                indexOut = listIn.index(row)
    

    fileOut = open("pz4out.txt", 'w', encoding='utf-8')
    for row in listIn:
        if listIn.index(row) == indexOut + 1:
            rowOut = row.replace("\n", "************\n")
            fileOut.write(rowOut)
        else:
            fileOut.write(row)

