import time

def sortByLevel(element):
    return element['priority']

num = int(input("Please input the number of process : "))
info = []
for i in range(num):
    t = int(input("Please input the time required for P"+str(i)+":"))
    level = int(input("Please input the priority of P"+str(i)+":"))
    info.append({'name':"P"+str(i),'priority':level,'time':t,'state':"R"})
info.sort(key=sortByLevel,reverse=True)
info_R = info[:]
print(info_R)
second = 0
while (info_R!=[]):
    second = second+1
    print("No." +str(second)+"s")
    print(info_R[0]['name'])
    info_R[0]['time']=info_R[0]['time']-1
    info_R[0]['priority']=info_R[0]['priority']-1
    if (info_R[0]['time']==0):
        info_R.pop(0)
    info_R.sort(key=sortByLevel,reverse=True)
    print(info_R)
    time.sleep(1)
print("Successful!")