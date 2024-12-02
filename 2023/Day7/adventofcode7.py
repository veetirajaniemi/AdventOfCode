def dircount():
    file = open("input7.txt", "r")
    currpath = [] # directories in current path
    directories = {}

    filename = 9999 # :D


    while(True):
        x = file.readline()
        string = x[:-1]
        strlen = len(string)

        if (strlen == 0):
            break

        if string[0:5] == "$ cd ": # some directory
            dir = string[5:strlen]
            if dir != "..":
                if dir not in directories.keys():
                    directories[dir] = 0
                else:
                    dir = str(filename)
                    directories[dir] = 0
                    filename += 1 
                    
                currpath.append(dir) # now we are here

            elif string[5:strlen] == "..":
                currpath.pop()

        elif string[0] != "d" and string[0] != "$":
            parts = string.split(" ")
            size = int(parts[0])
            for i in currpath:
                directories[i] += size

    sum = 0    

    maxspace = 70000000 # the maximum space available
    required = 30000000 # required free space

    used = directories["/"] # space used now
    minval = maxspace 
    

    for i in directories.values():
        if i <= 100000:
            sum += i # part 1
        
        nowused = used-i # used space if current dir was deleted
        unused = maxspace-nowused # unused space

        if (required < unused < minval):
            minval = unused
            bestval = i
  

    print(f"The sum of asked sizes: {sum}")
    print(f"The size of best dir to delete: {bestval}")


dircount()