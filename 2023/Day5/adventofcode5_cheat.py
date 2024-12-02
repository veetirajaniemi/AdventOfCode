def main():
    l1 = ["D","B","J","V"]
    l2 = ["P","V","B","W","R","D","F"]
    l3 = ["R","G","F","L","D","C","W","Q"]
    l4 = ["W","J","P","M","L","N","D","B"]
    l5 = ["H","N","B","P","C","S","Q"]
    l6 = ["R","D","B","S","N","G"]
    l7 = ["Z","B","P","M","Q","F","S","H"]
    l8 = ["W","L","F"]
    l9 = ["S","V","F","M","R"]
    lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

    input = open("input5.txt","r")
    for i in range(0,10):
        input.readline()

    while(True):
        x = input.readline()
        str = x[:-1]
        if (len(str) == 0):
            break
        parts = str.split(" ")
        numberof = int(parts[1]) # how many to move
        num1 = int(parts[3]) # from
        num2 = int(parts[5]) # to

        # moved = lists[num1-1][-numberof:]
        # for i in range(0,numberof):
        #     if (len(lists[num1-1]) > 0):
        #         lists[num1-1].pop()
        
        # lists[num2-1] += moved

        for i in range(0,numberof): # PART 1
            list1 = lists[num1-1]
            list2 = lists[num2-1]
            moved = list1.pop()
            list2.append(moved)

    for i in range(0,len(lists)):
        cur = lists[i]
        print(cur[-1], end = "")

main()