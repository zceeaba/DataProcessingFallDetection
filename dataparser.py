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

from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)
"""
wearablestore={}
store=[]
with open('wearable.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
db = client.wearable
parameters = db.parameters
for i in range(len(json_data)):
    dictless={}
    #print(json_data[i])
    if json_data[i].get('e'):
        uid=json_data[i]["uid"][-2:]
        t = json_data[i]["e"][0]["t"]
        accel = json_data[i]["e"][0]["v"]
        id = json_data[i]["_id"]["$oid"]
        timestamp = json_data[i]["bt"]["$date"]
        if uid=="c0" or uid=="c1":
            t=t/2
            parsedtimestamp = dateutil.parser.parse(timestamp)
            result = parsedtimestamp - datetime.timedelta(seconds=t)
            dictless["id"]=id
            dictless["uid"]=uid
            dictless["result"]=result
            dictless["acceleration"]=accel
        parsedtimestamp = dateutil.parser.parse(timestamp)
        result = parsedtimestamp - datetime.timedelta(seconds=t)
        dictless["id"]=id
        dictless["uid"]=uid
        dictless["result"]=result
        dictless["acceleration"]=accel
        print(i)
    #wearablestore[str(i)]=dictless
    store.append(dictless)
parameters.insert_many(store)
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
    print(mul,mulend)
    keys=(i for i in range(jumps[mul],jumps[mulend]))
    dictionarystore={str(k):dictionarystore[str(k)] for k in keys}
    #print(itemstore)
    jeys=(i for i in range(jumps[mul],jumps[mulend]))
    itemstore={str(j):itemstore[str(j)] for j in jeys}
    videoarray.append(dictionarystore)
    itemsarray.append(itemstore)
    """
#print(videoarray)
#print(itemsarray)
videocolin.insert_many(videoarray)
itemscolin.insert_many(itemsarray)
