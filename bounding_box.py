import json
import dateutil
import numpy
import dateutil.parser
import pandas as pd

with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]

object_id = []
bounding_box = []
bounding_box_center = []
silhouette = []
no_sil = []
my_list = []

#combo=pd.DataFrame(columns=['timestamp', 'silhouette', '2Dbb', '2Dbbcen'])
def returnrecord():
    finaldata = {}
    for i in range(len(json_data)):
        time_stamp=dateutil.parser.parse(json_data[i]["bt"]["$date"]).replace(tzinfo=None)
        finaldata[time_stamp]=[]

    for i in range(len(json_data)):
        time_stamp=dateutil.parser.parse(json_data[i]["bt"]["$date"]).replace(tzinfo=None)
        #timestr = time_stamp.strftime("%Y%m%d%H%M%S")
        for ele in range(len(json_data[i]["e"])):
            if json_data[i]["e"][ele]["n"] == "silhouette":
                silhouette.append(json_data[i]["_id"]["$oid"])
                sil=json_data[i]["e"][ele]["v"]
                finaldata[time_stamp].append(sil)
            else:
                no_sil.append(i)
        for ele in range(len(json_data[i]["e"])):
            if json_data[i]["e"][ele]["n"] == "2Dbb":
                object_id.append(json_data[i]["_id"]["$oid"])
                bounding_box.append(json_data[i]["e"][ele]["v"])
                bounding_box_center.append(json_data[i]["e"][ele + 1]["v"])
                twodbb=json_data[i]["e"][ele]["v"]
                #twodbbcen=json_data[i]["e"][ele + 1]["v"]
                finaldata[time_stamp].append(twodbb)
            if json_data[i]["e"][ele]["n"]=="2DCen":
                twodbbcen=json_data[i]["e"][ele]["v"]
                finaldata[time_stamp].append(twodbbcen)
    return finaldata

#print(finaldata)
#print(len(finaldata.keys()))
#combo=pd.DataFrame(finaldata,columns=['silhouette','2dbb','2dbbcen'])
#print(combo)
"""
time_stamp = []
for i in range(len(json_data)):
    time_stamp.append(json_data[i]["bt"]["$date"])

cleaned_time_stamp = []
for i in time_stamp: 
    cleaned_time_stamp.append(dateutil.parser.parse(i).replace(tzinfo=None))

numpy_time_stamp = numpy.array(cleaned_time_stamp)
arr = numpy.diff(numpy_time_stamp)
print(numpy_time_stamp[:6])
print(arr[:5])
#import numpy
#
#x = numpy.array(no_sil)
#arr = numpy.diff(x)
#for i, e in enumerate(arr):
#    if e == 1:
#        my_list.append(no_sil[i - 1])
"""