def main():
    input = open("input5.txt","r")
    lists = [[] for i in range(0,9)]
    
    for i in range(0,8):
        x = input.readline()
        str = x[:-1]
        if (len(str) == 0):
            break
        letters = str[1::4]
        
        for j in range(0,len(letters)):
            if letters[j] != " ":
                lists[j].append(letters[j])

    for i in range(0,2):
        input.readline()

    for i in lists:
        i.reverse()

    while(True):
        x = input.readline()
        str = x[:-1]
        if (len(str) == 0):
            break
        parts = str.split(" ")
        numberof = int(parts[1]) # how many to move
        num1 = int(parts[3]) # from
        num2 = int(parts[5]) # to

        moved = lists[num1-1][-numberof:]
        for i in range(0,numberof):
            if (len(lists[num1-1]) > 0):
                lists[num1-1].pop()
        
        lists[num2-1] += moved

        # for i in range(0,numberof): # PART 1
        #     list1 = lists[num1-1]
        #     list2 = lists[num2-1]
        #     moved = list1.pop()
        #     list2.append(moved)

    for i in range(0,len(lists)):
        cur = lists[i]
        print(cur[-1], end = "")
        


main()