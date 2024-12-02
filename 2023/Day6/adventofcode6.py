def findindex(length):
    input = open("input6.txt", "r")
    line = input.readline()
    str = list(line[:-1])

    index = 0 # index in string list
    chars = []
    
    while(True):
        
        if (chars.count(str[index]) > 0):
            remindex = chars.index(str[index])
            del chars[0:remindex+1] # remove from start to first duplicate value

        chars.append(str[index]) # not duplicates, can add
        
        if (len(chars) == length):
            print(f"Index found: {index+1}")
            return

        index += 1


findindex(4)
findindex(14)