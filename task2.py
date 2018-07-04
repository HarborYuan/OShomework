import time
mem = []
blank = [(0,128*1024-1)]

while (True):
    x = int(input("Please input the operation number:\n1:show\n2:allocate\n3:free\n0:quit\n"))
    if (x==0):
        break
    if (x==1):
        print(blank)
        time.sleep(1)
        continue
    if (x==2):
        size = input("Please input the size of mem you want:\n")
        if (size[-1]=='k'):
            size = int(size[0:-1])*1024
        else:
            size = int(size)
        isAllo = False
        for i in range(len(blank)):
            if (blank[i][1]-blank[i][0]+1==size):
                mem.append(blank[i])
                blank.pop(i)
                isAllo = True
                break
            if (blank[i][1]-blank[i][0]+1)>size:
                mem.append((blank[i][0],blank[i][0]+size-1))
                blank[i]=(blank[i][0]+size,blank[i][1])
                isAllo = True
                break
        if (isAllo):
            print("Success!")
        else:
            print("Error!")
        mem.sort()
        blank.sort()
    if (x==3):
        print("Allocated mem")
        for i in range(len(mem)):
            print("No."+str(i)+': '+str(mem[i]))
        x = int(input("Please choose the index of part you want to free :\n"))
        blank.append(mem.pop(x))
        blank.sort()
        i = 0
        while(i < (len(blank)-1)):
            if (blank[i][1]==blank[i+1][0]-1):
                blank[i]=(blank[i][0],blank[i+1][1])
                blank.pop(i+1)
                i-=1
            i+=1



                
                

