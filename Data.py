import time
import datetime
#from datetime import datetime,timedelta
localtime= datetime.datetime.now()
#print("本地时间为：",localtime)
localtimes = datetime.datetime(2019,5,5)
#print((localtime-localtimes).days)
data = open("C:Data//data.txt","r")

list = []
listtid = []
listuid = []
listuids = []
listtids = []

lists = {}
listtyle = {}
listtime = {}

lists7 = {}
listtyle7 = {}
listtime7 = {}

lists30 = {}
listtyle30 = {}
listtime30 = {}


lists90 = {}
listtyle90 = {}
listtime90 = {}


lists180 = {}
listtyle180 = {}
listtime180 = {}

lists365 = {}
listtyle365 = {}
listtime365 = {}


for line in  data.readlines():
    lines = eval(line)

    listtid.append(lines['TId'])
    listuid.append(lines['UId'])
    i = str(lines['TId'])

    if(str(lines['TId']) in lists):
        if not lines['UId'] in lists[i]:
           lists[i].append(lines['UId'])
        #print(lists)
    else:
        lists[i] = []
        lists[i].append(lines['UId'])
        #print(lists)

    if(i in listtyle ):
        listtyle[i].append(lines['Style'])
    else:
        listtyle[i] = []
        listtyle[i].append(lines['Style'])

    if (i in listtime):
        listtime[i].append(lines['time'])
    else:
        listtime[i] = []
        listtime[i].append(lines['time'])
    #if(lines['TId'] == 1) :
        list.append(lines['UId'])
    #print(lines["Day"])
    strs = lines['Day'].split('/')
    #localtimes = datetime.datetime(string.atoi(strs[0]),string.atoi(strs[1]),string.atoi(str[2]))
    localtimes = datetime.datetime(int(strs[0]), int(strs[1]), int(strs[2]))

    #print(localtimes)
    #cha = timedelta(localtime-localtimes)
    #print(type(localtime-localtimes))
    cha = localtime - localtimes
    chb = datetime.timedelta(7)
    #print(cha <= chb)

    if(cha <= chb):
        if (str(lines['TId']) in lists7):
            if not lines['UId'] in lists7[i]:
                lists7[i].append(lines['UId'])
            # print(lists)
        else:
            lists7[i] = []
            lists7[i].append(lines['UId'])
            # print(lists)

        if (i in listtyle7):
            listtyle7[i].append(lines['Style'])
        else:
            listtyle7[i] = []
            listtyle7[i].append(lines['Style'])

        if (i in listtime7):
            listtime7[i].append(lines['time'])
        else:
            listtime7[i] = []
            listtime7[i].append(lines['time'])
    cha = localtime - localtimes
    chb = datetime.timedelta(30)
    # print(cha)
    # print(chb)
    # print(cha <= chb)
    if (cha <= chb):
            if (str(lines['TId']) in lists30):
                if not lines['UId'] in lists30[i]:
                    lists30[i].append(lines['UId'])
                # print(lists)
            else:
                lists30[i] = []
                lists30[i].append(lines['UId'])
                # print(lists)

            if (i in listtyle30):
                listtyle30[i].append(lines['Style'])
            else:
                listtyle30[i] = []
                listtyle30[i].append(lines['Style'])

            if (i in listtime30):
                listtime30[i].append(lines['time'])
            else:
                listtime30[i] = []
                listtime30[i].append(lines['time'])



    cha = localtime - localtimes
    chb = datetime.timedelta(90)
        # print(cha <= chb)

    if (cha <= chb):
            if (str(lines['TId']) in lists90):
                if not lines['UId'] in lists90[i]:
                    lists90[i].append(lines['UId'])
                # print(lists)
            else:
                lists90[i] = []
                lists90[i].append(lines['UId'])
                # print(lists)

            if (i in listtyle90):
                listtyle90[i].append(lines['Style'])
            else:
                listtyle90[i] = []
                listtyle90[i].append(lines['Style'])

            if (i in listtime90):
                listtime90[i].append(lines['time'])
            else:
                listtime90[i] = []
                listtime90[i].append(lines['time'])

    cha = localtime - localtimes
    chb = datetime.timedelta(180)
        # print(cha <= chb)

    if (cha <= chb):
            if (str(lines['TId']) in lists180):
                if not lines['UId'] in lists180[i]:
                    lists180[i].append(lines['UId'])
                # print(lists)
            else:
                lists180[i] = []
                lists180[i].append(lines['UId'])
                # print(lists)

            if (i in listtyle180):
                listtyle180[i].append(lines['Style'])
            else:
                listtyle180[i] = []
                listtyle180[i].append(lines['Style'])

            if (i in listtime180):
                listtime180[i].append(lines['time'])
            else:
                listtime180[i] = []
                listtime180[i].append(lines['time'])


    cha = localtime - localtimes
    chb = datetime.timedelta(365)
        #print(cha <= chb)


    if (cha <= chb):
            if (str(lines['TId']) in lists365):
                if not lines['UId'] in lists365[i]:
                    lists365[i].append(lines['UId'])
                # print(lists)
            else:
                lists365[i] = []
                lists365[i].append(lines['UId'])
                # print(lists)

            if (i in listtyle365):
                listtyle365[i].append(lines['Style'])
            else:
                listtyle365[i] = []
                listtyle365[i].append(lines['Style'])

            if (i in listtime365):
                listtime365[i].append(lines['time'])
            else:
                listtime365[i] = []
                listtime365[i].append(lines['time'])
    #print(lines)


#print("-----")
#print(listtid)
for i in listtid:
    if not i in listtids:
        listtids.append(i)
#print(listtids)


#print("-----")
#print(listuid)
for i in listuid:
    if not i in listuids:
        listuids.append(i)
#print(listuids)

#print("-----")
# print(lists)
# print(listtyle)
# print(listtime)
numcount = {}
tylecount = {}
tylescount = {}
timecount = {}

numcount7 = {}
tylecount7 = {}
tylescount7 = {}
timecount7 = {}

numcount30 = {}
tylecount30 = {}
tylescount30 = {}
timecount30 = {}


numcount90 = {}
tylecount90 = {}
tylescount90 = {}
timecount90 = {}


numcount180 = {}
tylecount180 = {}
tylescount180 = {}
timecount180 = {}

numcount365 = {}
tylecount365 = {}
tylescount365 = {}
timecount365 = {}


for key in lists.keys():
    numcount[key] = len(lists[key])

for key in listtyle:
    tylecount[key] = []
    for i in range(5):
        tylecount[key].append(listtyle[key].count(i+1))

for key in tylecount:
    tylescount[key] = []
    count = 0
    for i in tylecount[key]:
        count += i;
    for i in tylecount[key]:
        tylescount[key].append(i/count)

for key in listtime:
    timecount[key] = 0
    for i in listtime[key]:
        timecount[key] += i



for key in lists7.keys():
    numcount7[key] = len(lists7[key])

for key in listtyle7:
    tylecount7[key] = []
    for i in range(5):
        tylecount7[key].append(listtyle7[key].count(i+1))

for key in tylecount7:
    tylescount7[key] = []
    count = 0
    for i in tylecount7[key]:
        count += i;
    for i in tylecount7[key]:
        tylescount7[key].append(i/count)

for key in listtime7:
    timecount7[key] = 0
    for i in listtime7[key]:
        timecount7[key] += i



for key in lists30.keys():
    numcount30[key] = len(lists30[key])

for key in listtyle30:
    tylecount30[key] = []
    for i in range(5):
        tylecount30[key].append(listtyle30[key].count(i+1))

for key in tylecount30:
    tylescount30[key] = []
    count = 0
    for i in tylecount30[key]:
        count += i;
    for i in tylecount30[key]:
        tylescount30[key].append(i/count)

for key in listtime30:
    timecount30[key] = 0
    for i in listtime30[key]:
        timecount30[key] += i




for key in lists90.keys():
    numcount90[key] = len(lists90[key])

for key in listtyle90:
    tylecount90[key] = []
    for i in range(5):
        tylecount90[key].append(listtyle90[key].count(i+1))

for key in tylecount90:
    tylescount90[key] = []
    count = 0
    for i in tylecount90[key]:
        count += i;
    for i in tylecount90[key]:
        tylescount90[key].append(i/count)

for key in listtime90:
    timecount90[key] = 0
    for i in listtime90[key]:
        timecount90[key] += i

for key in lists180.keys():
    numcount180[key] = len(lists180[key])

for key in listtyle180:
    tylecount180[key] = []
    for i in range(5):
        tylecount180[key].append(listtyle180[key].count(i+1))

for key in tylecount180:
    tylescount180[key] = []
    count = 0
    for i in tylecount180[key]:
        count += i;
    for i in tylecount180[key]:
        tylescount180[key].append(i/count)

for key in listtime180:
    timecount180[key] = 0
    for i in listtime180[key]:
        timecount180[key] += i

for key in lists365.keys():
    numcount365[key] = len(lists365[key])

for key in listtyle365:
    tylecount365[key] = []
    for i in range(5):
        tylecount365[key].append(listtyle365[key].count(i+1))

for key in tylecount365:
    tylescount365[key] = []
    count = 0
    for i in tylecount365[key]:
        count += i;
    for i in tylecount365[key]:
        tylescount365[key].append(i/count)

for key in listtime365:
    timecount365[key] = 0
    for i in listtime365[key]:
        timecount365[key] += i
firesun ={}
firesun["7"] = {}
firesun["7"]["count"]={}
firesun["7"]["tyle"] ={}
firesun["7"]["time"] ={}

for key in numcount7.keys():
    firesun["7"]["count"][key] = numcount7[key]
for key in tylescount7.keys():
    firesun["7"]["tyle"][key] = tylescount7[key]
for key in timecount7.keys():
    firesun["7"]["time"][key] = timecount7[key]

firesun["30"] = {}
firesun["30"]["count"]={}
firesun["30"]["tyle"] ={}
firesun["30"]["time"] ={}
for key in numcount30.keys():
    firesun["30"]["count"][key] = numcount30[key]
for key in tylescount7.keys():
    firesun["30"]["tyle"][key] = tylescount30[key]
for key in timecount7.keys():
    firesun["30"]["time"][key] = timecount30[key]


firesun["90"] = {}
firesun["90"]["count"]={}
firesun["90"]["tyle"] ={}
firesun["90"]["time"] ={}

for key in numcount90.keys():
    firesun["90"]["count"][key] = numcount90[key]
for key in tylescount90.keys():
    firesun["90"]["tyle"][key] = tylescount90[key]
for key in timecount90.keys():
    firesun["90"]["time"][key] = timecount90[key]


firesun["180"] = {}
firesun["180"]["count"]={}
firesun["180"]["tyle"] ={}
firesun["180"]["time"] ={}

for key in numcount180.keys():
    firesun["180"]["count"][key] = numcount180[key]
for key in tylescount180.keys():
    firesun["180"]["tyle"][key] = tylescount180[key]
for key in timecount180.keys():
    firesun["180"]["time"][key] = timecount180[key]

firesun["365"] = {}
firesun["365"]["count"]={}
firesun["365"]["tyle"] ={}
firesun["365"]["time"] ={}

for key in numcount365.keys():
    firesun["365"]["count"][key] = numcount365[key]
for key in tylescount365.keys():
    firesun["365"]["tyle"][key] = tylescount365[key]
for key in timecount365.keys():
    firesun["365"]["time"][key] = timecount365[key]

firesun["all"] = {}

firesun["all"]["count"]={}
firesun["all"]["tyle"] ={}
firesun["all"]["time"] ={}

for key in numcount.keys():
    firesun["all"]["count"][key] = numcount[key]
for key in tylescount.keys():
    firesun["all"]["tyle"][key] = tylescount[key]
for key in timecount.keys():
    firesun["all"]["time"][key] = timecount[key]

#print(firesun)

if __name__ == '__main__':
    for i in firesun:
        print(firesun[i])

#for i in range(6):

# print(numcount)1
# print(tylecount)



# print(tylescount)
# print(timecount)

# print(numcount7)
# print(tylecount7)
# print(tylescount7)
# print(timecount7)

#print(list)








#line = data.readline()
#print (line)
# while line:
#     #print (line)
#     line= data.readline()



