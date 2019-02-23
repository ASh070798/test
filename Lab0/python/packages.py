packages = []
expack = []
trigger = False
MyFile = open('data.txt')
for line in MyFile:
    packages.append(int(line))
    for i in range(min(packages),max(packages)):
        for e in packages:
            if e==i:
                trigger = True
                break
            else:
                trigger = False
        if trigger==False:
            for e in expack:
                if e==i:
                    trigger = True
                    break
                else:
                    trigger = False
            if trigger==False:
                expack.append(i)
    if expack==[]:
        print("Message "+str(min(packages))+"-"+str(max(packages))+" has been recieved!")
    else:
        print("Message "+str(min(packages))+"-"+str(max(packages))+" doesn't contain next packages: ")
        print(expack)
    expack = []    
MyFile.close()       


