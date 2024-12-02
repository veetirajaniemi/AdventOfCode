
if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    
    floor = 0
    found = False
    for i in range(len(data[0])):
        if data[0][i] == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1 and not found:
            index = i + 1
            found = True
    
    print(floor)
    print(index)