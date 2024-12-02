def main():
    tiedosto = open("input1.txt", "r")
    sum = 0
    max = 0
    max2 = 0
    max3 = 0

    while(True):
        rivi = tiedosto.readline()
        num = rivi[:-1]
        if (len(rivi) < 1):
            break
        elif (len(num) == 0):
            if (sum > max):
                max3 = max2
                max2 = max
                max = sum          
            elif (sum > max2):
                max3 = max2
                max2 = sum
            elif(sum > max3):
                max3 = sum
            sum = 0
        else:
            sum = sum + int(num)

    ans = max+max2+max3
    print(ans)
main()