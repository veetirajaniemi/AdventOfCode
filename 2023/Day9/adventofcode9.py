def positions():
    input = open("input9.txt", "r")

    positions = []
    
    tail = [0,0] # positions as x and y coordiantes
    head = [0,0]
    positions.append(tail)
    print(positions)
    lastdir = ""

    while(True):
        x = input.readline()
        str = x[:-1]
        if (len(str) == 0):
            break

        dir = str[0]
        steps = int(str[2:len(str)])

        if dir == "L": # left
            head[0] -= steps

            for i in range(0,steps):
                tail[0] -= 1
                temp = tail[:]
                print(tail)
                positions.append(tail[:])
                # if positions.count(temp[:]) == 0:
                #     positions.append(tail[:])

        elif dir == "R": # right
            head[0] += steps
        elif dir == "U": # up
            head[1] += steps
        else: # down
            head[1] -= steps

        lastdir = dir

    



positions()