def main():
    tiedosto = open("input2.txt","r")
    wins = 0
    points = 0
    # x y z lose draw win
    while(True):
        rivi = tiedosto.readline()
        arvot = rivi[:-1]

        if (len(arvot) == 0):
            break
         
        if (arvot[0] == "A"): # rock
            if (arvot[2] == "X"): # lose + scissors
                points += 3
            elif (arvot[2] == "Y"): # draw + rock
                points += 4
            else: # win + paper
                points += 8
        elif(arvot[0] == "B"): # paper
            if (arvot[2] == "X"): # lose + rock
                points += 1
            elif(arvot[2] == "Y"): # draw + paper
                points += 5
            else: # win + scissors
                points += 9
        else: # scis
            if (arvot[2] == "X"): # lose + paper
                points += 2
            elif (arvot[2] == "Y"): # draw + scis
                points += 6
            else: # win + rock
                points += 7

    print(points)

main()