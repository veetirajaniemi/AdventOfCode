import string


def main():
    tiedosto = open("input3.txt","r")
    pienet = list(string.ascii_lowercase)
    isot = list(string.ascii_uppercase)
    summa = 0
    while(True):

        x = tiedosto.readline()
        jono = x[:-1]
        if (len(jono) == 0):
            break
    
        pituus = int(len(jono)/2)
        osa1 = list(jono[0:pituus])
        osa2 = list(jono[pituus:len(jono)])
        

        for i in osa1:
            if i in osa2:
                if i in pienet:
                    summa += (pienet.index(i) + 1)

                if i in isot:
                    summa += (isot.index(i) + 27)

                break

    print(summa)

main()