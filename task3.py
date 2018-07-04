map = [0 for i in range(8*2*4)]


while(True):
    x = int(input("Please input the operation number:\n1:get\n2:free\n3:show\n0:quit\n"))
    if (x==0):
        break
    if (x==1):
        map_index = []
        file_size = int(input("Please input the file size\n"))
        for i in range(8*2*4):
            if (map[i]==0):
                map_index.append(i)
        if (len(map_index)>=file_size):
            for i in map_index[0:file_size]:
                map[i] = 1
                print("------")
                print("logic address "+str(i)+" allocated")
                print("cylinder number: "+str(i // 8))
                print("track number: "+str((i % 8) // 4))
                print("sector number: "+str(i % 4))
                print("-------")
        else:
            print("Fail")
    if (x==2):
        cn = int(input("cylinder number: \n"))
        tn = int(input("track number: \n"))
        sn = int(input("sector number: \n"))
        print("The logic address is : "+str(8*cn+tn*4+sn))
        if (map[8*cn+tn*4+sn]==1):
            print("Success!")
            map[8*cn+tn*4+sn]=0
        else:
            print("Error!")
    if (x==3):
        ans=""
        for i in range(8):
            for j in range(4*2):
                ans+=str(map[i*8+j])
            ans+="\n"
        print(ans)