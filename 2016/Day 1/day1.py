import numpy as np



# N, E, S, W

def findLoc(data):
    currloc = [0, 0]
    locations = []
    locations.append(currloc.copy())
    dirindex = 0

    found = False

    for val in data:
        if dirindex == 0: # facing north
            if val[0] == 'R':
                for _ in range(int(val[1:-1])):
                    currloc[0] += 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex += 1
            elif val[0] == 'L':
                for _ in range(int(val[1:-1])):
                    currloc[0] -= 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex = 3

        elif dirindex == 1: # facing east
            if val[0] == 'R':
                for _ in range(int(val[1:-1])):
                    currloc[1] -= 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex += 1
            elif val[0] == 'L':
                for _ in range(int(val[1:-1])):
                    currloc[1] += 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex -= 1

        elif dirindex == 2: # facing south
            if val[0] == 'R':
                for _ in range(int(val[1:-1])):
                    currloc[0] -= 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex += 1
            elif val[0] == 'L':
                for _ in range(int(val[1:-1])):
                    currloc[0] += 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex -= 1
        
        elif dirindex == 3: # facing west
            if val[0] == 'R':
                for _ in range(int(val[1:-1])):
                    currloc[1] += 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex = 0
            elif val[0] == 'L':
                for _ in range(int(val[1:-1])):
                    currloc[1] -= 1
                    if currloc in locations and found == False:
                        part2loc = currloc.copy()
                        found = True
                    locations.append(currloc.copy())
                dirindex -= 1

    return currloc, part2loc


if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.readlines()    
    
    data = []
    for line in file:
        line = line.split(' ')
        data.append(line)

    data = data[0]
    

    finalLoc, part2loc = findLoc(data)

    print(finalLoc)
    print(part2loc)

    print(sum(np.abs(finalLoc)))
    print(sum(np.abs(part2loc)))

    

