import json
from datetime import datetime
import datetime
import dateutil.parser
import pymongo
import numpy as np
from matplotlib import pyplot as plt
#client = MongoClient()
#client=pymongo.MongoClient('mongodb+srv://jayab96:H32yTpSBGi4xhVTO@ads-z5r3r.mongodb.net/')
#client = MongoClient(<Atlas connection string>)

#client = pymongo.MongoClient('mongodb://localhost:27017/')
def wearable():
    wearablestore={}
    store=[]
    with open('wearable.json', 'r') as handle:
        json_data = [json.loads(line) for line in handle]
    #db = client.wearabletest
    #parameters = db.parameters
    finallist=[]
    finallistb=[]
    xlist, ylist, zlist = [], [], []
    xtlist,ytlist,ztlist=[],[],[]
    xlista, ylista, zlista = [], [], []
    xtlista,ytlista,ztlista=[],[],[]
    tlist=[]
    falls={}
    flag=3
    groundnewlist=[]
    groundnewlistb=[]
    groundtlist=[]
    groundtlistb=[]
    for i in range(len(json_data)):
        importantdict = {}
        dictless={}
        #startimes=[17:27:56,17:15:56]
        #times={[8,10,21,23],[41s,45s,57,61],[75,80,93,97],[110,114,126,129],[142,146,159,164],[178,183,195,198],[219,222,234,237],[258,262,274,278],[299,303,313,317],[332,335,349,353],[378,382,392,396],[420,424,435,440],[452,456,466,470],[486,491,501,507]}
        #timesb=[[8,10,21,25],[36,39,53,56],[68,72,86,91],[99,102,118,122],[134,138,151,155],[168,173,190,192],[210,212,230,235],[249,252,269,272],[281,283,302,306],[317,320,339,342],[357,360,373,377],[391,394,410,413],[426,429,443,446],[456,459,471,474]]
        #print(json_data[i])
        if json_data[i].get('e'):
            uid=json_data[i]["uid"][-2:]
            t = json_data[i]["e"][0]["t"]
            accel=[0,0,0]
            id = json_data[i]["_id"]["$oid"]
            timestamp = json_data[i]["bt"]["$date"]
            for j in range(len(json_data[i]["e"])):
                v=json_data[i]["e"][j]["v"]
                if len(v)>0:
                    accel[0] += json_data[i]["e"][j]["v"][0]
                    accel[1] += json_data[i]["e"][j]["v"][1]
                    accel[2] += json_data[i]["e"][j]["v"][2]
                #print(accel)
            #previousaccelx.append(accel[0])
            #previousaccely.append(accel[1])
            #previousaccelz.append(accel[2])
            if uid=="c0" or uid=="c1":
                t=t/2
                parsedtimestamp = dateutil.parser.parse(timestamp)
                result = parsedtimestamp - datetime.timedelta(seconds=t)
                dictless["id"]=id
                dictless["uid"]=uid
                dictless["result"]=result
                dictless["acceleration"]=accel
                dictless["accelerationx"]=accel[0]
                dictless["accelerationy"]=accel[1]
                dictless["accelerationz"]=accel[2]
            else:
                parsedtimestamp = dateutil.parser.parse(timestamp)
                result = parsedtimestamp - datetime.timedelta(seconds=t)
                dictless["id"]=id
                dictless["uid"]=uid
                dictless["result"]=result
                dictless["acceleration"]=accel
                dictless["accelerationx"]=accel[0]
                dictless["accelerationy"]=accel[1]
                dictless["accelerationz"]=accel[2]
            #dictless["groundtruthstate"]=3
            fallstate=[0,1,2,3]
            parsedtimestamp = dateutil.parser.parse(timestamp)
            naive = parsedtimestamp.replace(tzinfo=None)
            times = [[8, 10, 21, 23], [41, 45, 57, 61], [75, 80, 93, 97], [110, 114, 126, 129], [142, 146, 159, 164],
                     [178, 183, 195, 198], [219, 222, 234, 237], [258, 262, 274, 278], [299, 303, 313, 317],
                     [332, 335, 349, 353], [378, 382, 392, 396], [420, 424, 435, 440], [452, 456, 466, 470],
                     [486, 491, 501, 507]]
            timesb = [[8, 10, 21, 25], [36, 39, 53, 56], [68, 72, 86, 91], [99, 102, 118, 122], [134, 138, 151, 155],
                      [168, 173, 190, 192], [210, 212, 230, 235], [249, 252, 269, 272], [281, 283, 302, 306],
                      [317, 320, 339, 342], [357, 360, 373, 377], [391, 394, 410, 413], [426, 429, 443, 446],
                      [456, 459, 471, 474]]

            if naive>datetime.datetime(2018, 3, 22, 17, 27, 56, 0) and naive<datetime.datetime(2018, 3, 22, 17,36,46 , 0) :
                if dictless["uid"]=="c0" or dictless["uid"]=="c1":
                    print(dictless["uid"])
                    for list in times:
                        for index in range(len(list)):
                            eventimestamp = datetime.datetime(2018, 3, 22, 17, 27, 56, 0) + datetime.timedelta(0, list[index])
                            checktime=(eventimestamp - naive).total_seconds()
                            #print(checktime)
                            if checktime<1 and checktime >-1:
                                dictless["groundtruthstate"]=index
                                flag=index
                    if flag == 1:
                        dictless["groundtruthstate"] = 1
                    elif flag == 2:
                        dictless["groundtruthstate"] = 2
                    elif flag == 0:
                        dictless["groundtruthstate"] = 0
                    else:
                        dictless["groundtruthstate"] = 3

                    if abs(dictless["acceleration"][0])>7:
                        #print(naive)
                        print("x: "+str(i))
                        xlist.append(dictless["acceleration"][0])
                        xtlist.append(i)
                    if  abs(dictless["acceleration"][1]) > 7:
                        #print(naive)
                        print("y: " + str(i))
                        ylist.append(dictless["acceleration"][1])
                        ytlist.append(i)
                    if abs(dictless["acceleration"][2]) > 7:
                        #print(naive)
                        print("z: " + str(i))
                        zlist.append(dictless["acceleration"][2])
                        ztlist.append(i)
                    importantdict["timestamp"]=naive
                    importantdict["groundtruth"]=dictless["groundtruthstate"]
                    groundnewlist.append(dictless["groundtruthstate"])
                    groundtlist.append(i)
                    #finallist.append(importantdict)
                    finallist.append(dictless)
            else:
                dictless["groundtruthstate"]=5
            if naive>datetime.datetime(2018, 3, 22, 17, 15, 56, 0) and naive<datetime.datetime(2018, 3, 22, 17,24,2 , 0) :
                if dictless["uid"]=="c0" or dictless["uid"]=="c1":
                    print(dictless["uid"])
                    for list in timesb:
                        for index in range(len(list)):
                            eventimestamp = datetime.datetime(2018, 3, 22, 17, 15, 56, 0) + datetime.timedelta(0, list[index])
                            checktime=(eventimestamp - naive).total_seconds()
                            #print(checktime)
                            if checktime<1 and checktime >-1:
                                dictless["groundtruthstate"]=index
                                flag=index

                    if flag == 1:
                        dictless["groundtruthstate"] = 1
                    elif flag == 2:
                        dictless["groundtruthstate"] = 2
                    elif flag == 0:
                        dictless["groundtruthstate"] = 0
                    else:
                        dictless["groundtruthstate"] = 3

                    if abs(dictless["acceleration"][0])>7:
                        print(naive)
                        print("x: "+str(i))
                        xlista.append(dictless["acceleration"][0])
                        xtlista.append(i)
                    if  abs(dictless["acceleration"][1]) > 7:
                        print(naive)
                        print("y: " + str(i))
                        ylista.append(dictless["acceleration"][1])
                        ytlista.append(i)
                    if abs(dictless["acceleration"][2]) > 7:
                        print(naive)
                        print("z: " + str(i))
                        zlista.append(dictless["acceleration"][2])
                        ztlista.append(i)
                    print(dictless["groundtruthstate"])
                    importantdict["timestamp"]=naive
                    importantdict["groundtruth"]=dictless["groundtruthstate"]
                    groundnewlistb.append(dictless["groundtruthstate"])
                    groundtlistb.append(i)
                    #finallistb.append(importantdict)
                    finallist.append(dictless)
            #else:
            #    dictless["groundtruthstate"]=5
    return finallist

def normalizedwearable(results):
    accelx,accely,accelz=[],[],[]
    print(results)
    for i in range(len(results)):
        accelx.append(results[i]["accelerationx"])
        accely.append(results[i]["accelerationy"])
        accelz.append(results[i]["accelerationz"])
    meanx=np.mean(np.array(accelx))
    meany=np.mean(np.array(accely))
    meanz=np.mean(np.array(accelz))
    stdx=np.std(np.array(accelx))
    stdy=np.std(np.array(accely))
    stdz=np.std(np.array(accelz))
    maxx=max(accelx)
    maxy=max(accely)
    maxz=max(accelz)
    print(meanx,meany,meanz,stdx,stdy,stdz)
    for i in range(len(results)):
        #results[i]["accelerationx"]=(results[i]["accelerationx"]-meanx)/stdx
        #results[i]["accelerationy"]=(results[i]["accelerationy"]-meany)/stdy
        #results[i]["accelerationz"]=(results[i]["accelerationz"]-meanz)/stdz
        results[i]["accelerationx"]=float(results[i]["accelerationx"])/maxx
        results[i]["accelerationy"]=float(results[i]["accelerationy"])/maxy
        results[i]["accelerationz"]=float(results[i]["accelerationz"])/maxz

    return results
"""

plt.scatter(xtlist,xlist)
plt.scatter(ytlist,ylist)
plt.scatter(ztlist,zlist)
plt.scatter(groundtlist,groundnewlist)
plt.show()
plt.scatter(xtlista,xlista)
plt.scatter(ytlista,ylista)
plt.scatter(ztlista,zlista)
plt.show()
"""


#wearablestore[str(i)]=dictless
#store.append(dictless)
#parameters.insert_many(finallist)

"""
#print(wearablestore)

#client = MongoClient('mongodb://localhost:27017/')
with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
jumps=[d for d in xrange(0, 115808, 10528)]
print(jumps)
videoarray=[]
itemsarray=[]
db = client.Video
videocolin = db.videocol
itemscolin = db.itemcol
for mul in range(len(jumps)-1):
    dictionarystore={}
    itemstore={}
    mulend=mul+1
    count=0
    for i in range(jumps[mul],jumps[mulend]):
        dictless={}
        id = json_data[i]["_id"]["$oid"]
        uid=json_data[i]["uid"]
        date=json_data[i]["bt"]["$date"]
        items = []
        #if hasattr(json_data[i],"e"):
        for item in json_data[i]["e"]:
            data = {}
            #print("haha")
            #print(item)
            if item["n"]=="silhouette":
                data["id"] = id
                data["type"]="silhouette"
                data["imagevalue"]=item["v"]
            else:
                data["id"] = id
                if item["n"]=="frameId":
                    data["type"]="frameId"
                    data["frameid"]=item["v"]
                elif item["n"]=="2Dbb":
                    data["type"]="2dboundingbox"
                    data["2dbbcoordinates"]=item["v"]
                elif item["n"]=="3Dbb":
                    data["type"]="3dboundingbox"
                    data["3dbbcoordinates"]=item["v"]
                elif item["n"]=="3Dcen":
                    data["type"]="3dcentre"
                    data["3dcencoordinates"]=item["v"]
                elif item["n"]=="2DCen":
                    data["type"]="2dcentre"
                    data["2dcencoordinates"]=item["v"]
                elif item["n"]=="Activity":
                    data["type"]="Activity"
                    data["activity"]=item["v"]
                elif item["n"]=="userID":
                    data["type"]="userID"
                    data["userid"]=item["v"]
            itemsarray.append(data)
        else:
            count+=1
        #dictless["items"]=items
        parsedtimestamp = dateutil.parser.parse(date)
        dictless["id"]=id
        dictless["uid"]=uid
        dictless["date"]=parsedtimestamp
        videoarray.append(dictless)
        #print(dictless)
        #print(count)
        #dictionarystore[str(i)]=dictless
        #print(items)
        #itemstore[str(i)]=items
        print(i)
    #tens=(l*10000 for l in range(5900))
    """
"""
    print(mul,mulend)
    keys=(i for i in range(jumps[mul],jumps[mulend]))
    dictionarystore={str(k):dictionarystore[str(k)] for k in keys}
    #print(itemstore)
    jeys=(i for i in range(jumps[mul],jumps[mulend]))
    itemstore={str(j):itemstore[str(j)] for j in jeys}
    videoarray.append(dictionarystore)
    itemsarray.append(itemstore)
    """
"""
videocolin.insert_many(videoarray)
itemscolin.insert_many(itemsarray)
"""