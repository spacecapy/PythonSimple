
execution = True

while execution:
    print("\nEnter the range that you want to find perfect numbers.\ne.g. \"0,9000\" will return all the perfect numbers from 0 to 9000.")
    r = input().split(",")

    #check input
    if len(r) != 2 or r[0] >= r[1]:
        print("\nIncorrect input, please enter it again.")
    else:
        r[1] = str(int(r[1])+1)
        pn = []
        for i in range(int(r[0]),int(r[1])):
            s = 0
            print(i)
            for j in range(1,i):
                if i%j == 0:
                    s = s+j
            if s == i:
                pn.append(s)
        print(pn, end=""),
        execution = False
