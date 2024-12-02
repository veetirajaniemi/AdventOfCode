import string

def main():
    tiedosto = open("input3.txt","r")
    pienet = list(string.ascii_lowercase)
    isot = list(string.ascii_uppercase)
    summa = 0
    luettu = 0
    while(True):
        x = tiedosto.readline()
        jono = x[:-1]
        if (len(jono) == 0):
            break

        if (luettu == 0):
            osa1 = list(jono)
            luettu = 1
        elif(luettu == 1):
            osa2 = list(jono)
            luettu = 2
        elif(luettu == 2):
            osa3 = list(jono)

            for i in osa1:
                if i in osa2 and i in osa3:
                    if i in pienet:
                        summa += pienet.index(i) + 1
                    else:
                        summa += isot.index(i) + 27
                    luettu = 0
                    break

    print(summa)

main()