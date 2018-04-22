from django.shortcuts import render,render_to_response
from django.http import HttpResponse

import json
from pprint import pprint
from datetime import datetime
import datetime
import dateutil.parser
from django.db import connections
import json
from datetime import datetime
import datetime
import dateutil.parser
import pymongo
from .models import Video,attributes


# Create your views here.
def index(request):

    dictionarystore = {}
    with open('video.json', 'r') as handle:
        json_data = [json.loads(line) for line in handle]
    print(len(json_data))

    for i in range(1000):
        dictless = {}
        id = json_data[i]["_id"]["$oid"]
        uid = json_data[i]["uid"]
        date = json_data[i]["bt"]["$date"]
        items = []
        for item in json_data[i]["e"]:
            data = {}
            if item["n"] == "silhouette":
                data["type"] = "silhouette"
                data["value"] = item["v"]
            else:
                if item["n"] == "frameId":
                    data["type"] = "frameId"
                    data["value"] = item["v"]
                elif item["n"] == "2Dbb":
                    data["type"] = "2dboundingbox"
                    data["value"] = item["v"]
                elif item["n"] == "3Dbb":
                    data["type"] = "3dboundingbox"
                    data["value"] = item["v"]
                elif item["n"] == "3Dcen":
                    data["type"] = "3dcentre"
                    data["value"] = item["v"]
                elif item["n"] == "2DCen":
                    data["type"] = "2dcentre"
                    data["value"] = item["v"]
                elif item["n"] == "Activity":
                    data["type"] = "Activity"
                    data["value"] = item["v"]
                elif item["n"] == "userID":
                    data["type"] = "userID"
                    data["value"] = item["v"]
            items.append(data)
        dictless["items"] = items
        parsedtimestamp = dateutil.parser.parse(date)
        dictless["id"] = id
        dictless["uid"] = uid
        dictless["date"] = parsedtimestamp
        # print(dictless)
        # print(count)
        v = Video(videoid=id, uid=uid, date=parsedtimestamp)
        v.save()
        items=filter(None, items)
        if len(items)>0:
            #print(items)
            for x in items:
                a = attributes(type=x["type"], value=x["value"], video=v)
                a.save()
        dictionarystore[str(i)] = dictless
        print(i)
        #v.save()


    #keys = (i for i in range(20))
    #dictionarystore = {str(k): dictionarystore[str(k)] for k in keys}

    """
    with open('wearable.json', 'r') as handle:
        json_data = [json.loads(line) for line in handle]
    for i in range(len(json_data)):
        dictless = {}
        id = json_data[i]["_id"]["$oid"]
        if hasattr(json_data[i], "e"):
            t = json_data[i]["e"][0]["t"]
            accel = json_data[i]["e"][0]["v"]
        else:
            t = 0
            accel = [0, 0, 0]
        timestamp = json_data[i]["bt"]["$date"]
        parsedtimestamp = dateutil.parser.parse(timestamp)
        result = parsedtimestamp - datetime.timedelta(seconds=t)
        dictless["id"] = id
        dictless["result"] = result
        dictless["acceleration"] = accel
        dictionarystore[i] = dictless
        #print(dictless.id, dictless.time, dictless.acceleration)
        dictionarystore[i]=dictless
        print dictionarystore
    """
    #return render_to_response('datavis/index.html', {'data': dictionarystore})
    return HttpResponse("done")