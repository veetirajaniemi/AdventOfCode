def main():
    tiedosto = open("input4.txt","r")
    lkm = 0 # osa1, toinen joukoista sisältyy kokonaan toiseen
    lkm2 = 0 # osa2, joukot ovat osittain päällekkäin

    while(True):
        x = tiedosto.readline()
        rivi = x[:-1]
        if (len(rivi) == 0):
            break
        joukot = rivi.split(",")
        numerot1 = joukot[0].split("-")
        numerot2 = joukot[1].split("-")
        num1 = int(numerot1[0])
        num2 = int(numerot1[1])
        num3 = int(numerot2[0])
        num4 = int(numerot2[1])
        
        if (num1 >= num3 and num2 <= num4): # 1. joukko sisältyy toiseen
            lkm += 1
        elif (num1 <= num3 and num2 >= num4): # 2. joukko sisältyy ensimmäiseen
            lkm += 1

        if (num3 <= num1 <= num4): # 1. joukon alkupiste
            lkm2 += 1
        elif (num1 <= num3 <= num2): # 2. joukon alkupiste
            lkm2 += 1
        
    
    print(lkm)
    print(lkm2)


main()