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
import matplotlib.pyplot as plt
import pymongo
from .models import Video,attributes
import pandas as pd

# Create your views here.
def index(request):
    wearable={}
    store = []
    accellist=[]
    timelist=[]
    with open('wearable.json', 'r') as handle:
        json_data = [json.loads(line) for line in handle]
    for i in range(len(json_data)):
        dictless = {}
        # print(json_data[i])
        if json_data[i].get('e'):
            uid = json_data[i]["uid"][-2:]
            t = json_data[i]["e"][0]["t"]
            accel = json_data[i]["e"][0]["v"]
            id = json_data[i]["_id"]["$oid"]
            timestamp = json_data[i]["bt"]["$date"]
            if uid == "c0" or uid == "c1":
                t = t / 2
            parsedtimestamp = dateutil.parser.parse(timestamp)
            result = parsedtimestamp - datetime.timedelta(seconds=t)
            dictless["id"] = id
            dictless["uid"] = uid
            dictless["result"] = result
            dictless["acceleration"] = accel
            result=result.replace(tzinfo=None)
            if result>datetime.datetime(2018, 03, 22, 17, 15, 57,000) and result<datetime.datetime(2018, 03, 22, 17, 16, 27,000 ):
                timesec=result.strftime('%H:%M:%S.%f')[:-3]
                timelist.append(timesec)
                accellist.append(accel)
            #wearable[timesec]=accel
            print(i)
        # wearablestore[str(i)]=dictless
    import pygal
    line_chart = pygal.Line()
    line_chart.title = 'acceleration change with respect to time'
    print(accellist)
    print(timelist)
    accelx,accely,accelz=[],[],[]
    for x in accellist:
        accelx.append(x[0])
        accely.append(x[1])
        accelz.append(x[2])
    #.plot(timelist,accelx)
    #plt.plot(timelist,accely)
    #plt.plot(timelist,accelz)
    #plt.show()


    #line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.x_labels=timelist
    line_chart.add('accelx',accelx)
    line_chart.add('accely',accely)
    line_chart.add('accelz',accelz)
    #line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    #line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    #line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    #line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])

    #return render_to_response('datavis/index.html', {'data': dictionarystore})
    #return render(request,'datavis/index.html')
    return HttpResponse(line_chart.render())

