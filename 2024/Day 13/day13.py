import numpy as np


def countTokens(buttonA_X, buttonA_Y, buttonB_X, buttonB_Y, prize_X, prize_Y, gold = False):   
    buttonA_X = int(buttonA_X)
    buttonA_Y = int(buttonA_Y)
    buttonB_X = int(buttonB_X)
    buttonB_Y = int(buttonB_Y)
    prize_X = int(prize_X)
    prize_Y = int(prize_Y)

    if gold:
        prize_X = prize_X + 10000000000000
        prize_Y = prize_Y + 10000000000000

    A = np.matrix([[buttonA_X, buttonB_X], [buttonA_Y, buttonB_Y]])
    b = np.matrix([[prize_X], [prize_Y]])
    inv = np.linalg.inv(A)
    x = inv * b

    x1 = round(x[0,0], 2)
    x2 = round(x[1,0], 2)



    if gold == False:
        if x1.is_integer() == False or x2.is_integer() == False or x1 > 100 or x2 > 100:
            return 0
        else:
            return x1 * 3 + x2
    
    if x1.is_integer() == False or x2.is_integer() == False:
            return 0
    else:
        return x1 * 3 + x2
    




   

if __name__ == "__main__":
    with open('input.txt') as f:

        silver = 0
        gold = 0

        while True:
            lines = [f.readline().strip() for _ in range(3)]
            if not lines[0]:
                break
            buttonA = lines[0]
            buttonB = lines[1]
            prize = lines[2]

            buttonA_X = buttonA.split('X+')[1].split(',')[0]
            buttonA_Y = buttonA.split('Y+')[1]

            buttonB_X = buttonB.split('X+')[1].split(',')[0]
            buttonB_Y = buttonB.split('Y+')[1]

            prize_X = prize.split('X=')[1].split(',')[0]
            prize_Y = prize.split('Y=')[1]


            silver += countTokens(buttonA_X, buttonA_Y, buttonB_X, buttonB_Y, prize_X, prize_Y)
            gold += countTokens(buttonA_X, buttonA_Y, buttonB_X, buttonB_Y, prize_X, prize_Y, True)

            f.readline()

    print(f"Silver: {silver}")
    print(f"Gold: {gold}")