import json
from datetime import datetime
import datetime
import dateutil.parser
import pymongo
"""
from django.core.management import settings
settings.configure()
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FallDetect.settings")
"""

class MyDict(dict):
    pass

"""
with open('wearable.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
for i in range(len(json_data)):
    dict=MyDict()
    dictless={}
    id = json_data[i]["_id"]["$oid"]
    if hasattr(json_data[i],"e"):
        t = json_data[i]["e"][0]["t"]
        accel = json_data[i]["e"][0]["v"]
    else:
        t=0
        accel=[0,0,0]
    timestamp = json_data[i]["bt"]["$date"]
    parsedtimestamp = dateutil.parser.parse(timestamp)
    result = parsedtimestamp - datetime.timedelta(seconds=t)
    dictless["id"]=id
    dictless["result"]=result
    dictless["acceleration"]=accel
    dictionarystore[i]=dictless

print(dictionarystore)
"""
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

#client = MongoClient('mongodb://localhost:27017/')
with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
jumps=[d for d in xrange(0, 115808, 10528)]
print(jumps)
videoarray=[]
itemsarray=[]
db = client.datavis
videocolin = db.videocol
itemscolin = db.itemcol
for mul in range(len(jumps)-1):
    dictionarystore={}
    itemstore={}
    mulend=mul+1
    count=0
    for i in range(jumps[mul],jumps[mulend]):
        dict=MyDict()
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
                data["type"]="silhouette"
                data["imagevalue"]=item["v"]
            else:
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
            items.append(data)
        else:
            count+=1
        #dictless["items"]=items
        parsedtimestamp = dateutil.parser.parse(date)
        dictless["id"]=id
        dictless["uid"]=uid
        dictless["date"]=parsedtimestamp
        #print(dictless)
        #print(count)
        dictionarystore[str(i)]=dictless
        #print(items)
        itemstore[str(i)]=items
        print(i)
    #tens=(l*10000 for l in range(5900))
    print(mul,mulend)
    keys=(i for i in range(jumps[mul],jumps[mulend]))
    dictionarystore={str(k):dictionarystore[str(k)] for k in keys}
    #print(itemstore)
    jeys=(i for i in range(jumps[mul],jumps[mulend]))
    itemstore={str(j):itemstore[str(j)] for j in jeys}
    videoarray.append(dictionarystore)
    itemsarray.append(itemstore)
#print(videoarray)
#print(itemsarray)
videocolin.insert_many(videoarray)
itemscolin.insert_many(itemsarray)
