def main():
    tiedosto = open("input2.txt","r")
    wins = 0
    points = 0
    while(True):
        rivi = tiedosto.readline()
        arvot = rivi[:-1]

        if (arvot == "A X"):
            points += 4

        elif (arvot == "A Y"):
            wins += 1
            points += 8

        elif (arvot == "A Z"):
            points += 3

        elif (arvot == "B X"):
            points += 1

        elif (arvot == "B Y"):
            points += 5

        elif (arvot == "B Z"):
            wins += 1
            points += 9

        elif (arvot == "C X"):
            wins += 1
            points += 7

        elif (arvot == "C Y"):
            points += 2

        elif (arvot  == "C Z"):
            points += 6

        if (len(arvot) == 0):
            break
    print(points)
main()
