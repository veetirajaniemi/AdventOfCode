
def countRobots(info, width, height, seconds):

    halfWidth = width // 2
    halfHeight = height // 2

    for _ in range(seconds):
        for i in range(len(info)):
            
            x = info[i][0] + info[i][2] # x += dx
            y = info[i][1] + info[i][3] # y += dy

            if x < 0:
                x = height + x
            elif x >= height:
                x = x - height
            if y < 0:
                y = width + y
            elif y >= width:
                y = y - width
            
            coords = (x, y, info[i][2], info[i][3])
            info[i] = coords

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
    seconds = 100

    for line in lines:
        pos = line.split(" ")[0]
        y = int(pos.split(",")[0].split("=")[1])
        x = int(pos.split(",")[1])
        vel = line.split(" ")[1]
        dy = int(vel.split("=")[1].split(",")[0])
        dx = int(vel.split("=")[1].split(",")[1])
        info.append((x, y, dx, dy))


    safetyFactor = countRobots(info, width, height, seconds)
    print(safetyFactor)