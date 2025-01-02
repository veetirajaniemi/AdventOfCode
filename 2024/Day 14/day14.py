import matplotlib.pyplot as plt
import numpy as np

def countRobots(info, width, height, seconds, gold = False):

    halfWidth = width // 2 # for quadrants
    halfHeight = height // 2

    devX = []
    devY = []
    allCoords = [None] * seconds

    for i in range(seconds): # for each second
        allX = []
        allY = []
        for j in range(len(info)): # for each robot
            
            x = info[j][0] + info[j][2] # x += dx
            y = info[j][1] + info[j][3] # y += dy
            
            # check out of bounds cases
            if x < 0:
                x = height + x
            elif x >= height:
                x = x - height
            if y < 0:
                y = width + y
            elif y >= width:
                y = y - width
            coords = (x, y, info[j][2], info[j][3])
            info[j] = coords

            if gold: # store all coordinates for each robot
                allX.append(x)
                allY.append(y)

        if gold: # store all coordinates for each second
            allXY = np.array([allX, allY])
            allCoords[i] = allXY

            # deviations of x and y coordinates for each second 
            # thought that this would give some nice information and found the pattern :)
            devX.append(np.std(allX)) 
            devY.append(np.std(allY)) 



    if gold:
        allCoords = np.array(allCoords)
        return devX, devY, allCoords

    else:

        quadrants = [0, 0, 0, 0]

        for coords in info:
            if coords[0] < halfHeight and coords[1] < halfWidth:
                quadrants[0] += 1
            elif coords[0] < halfHeight and coords[1] > halfWidth:
                quadrants[1] += 1
            elif coords[0] > halfHeight and coords[1] < halfWidth:
                quadrants[2] += 1
            elif coords[0] > halfHeight and coords[1] > halfWidth:
                quadrants[3] += 1

        safetyFactor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
        return safetyFactor


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    info = []
    width = 101
    height = 103
    seconds = 10000

    for line in lines:
        pos = line.split(" ")[0]
        # for some reason i switched x and y, more like rows and columns with matrices :D
        y = int(pos.split(",")[0].split("=")[1])
        x = int(pos.split(",")[1]) 
        vel = line.split(" ")[1]
        dy = int(vel.split("=")[1].split(",")[0])
        dx = int(vel.split("=")[1].split(",")[1])
        info.append((x, y, dx, dy))

    # NOTE TO MYSELF: DO NOT RUN THE SILVER BEFORE THE GOLD AND BE AMAZED BY THE TOO HIGH ANSWER FOR GOLD....
    # safetyFactor = countRobots(info, width, height, seconds)
    # print("Silver: ", safetyFactor)

    # Plotting the deviations of x and y coordinates for each second to find the second where something interesting happens
    devX, devY, allCoords = countRobots(info, width, height, seconds, gold = True)
    fig, axs = plt.subplots(2)
    axs[0].plot(devX)
    axs[1].plot(devY)
    plt.show()
    for i in range(len(devX)):
        if devX[i] < 25 and devY[i] < 25: # found that the deviations are less than 25 at some points "randomly"
            print("Gold: ", i + 1) # i + 1 because the first second is 0 (another note to myself, not i - 1...)
            goldindex = i
            plt.figure()
            plt.scatter(allCoords[goldindex,0,:], allCoords[goldindex,1,:])
            plt.show()
            break

    