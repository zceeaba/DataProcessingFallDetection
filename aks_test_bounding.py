import json
import dateutil
import numpy
import datetime

with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]

object_id = []
bounding_box = []
bounding_box_center = []
silhouette = []
no_sil = []
my_list = []

for i in range(len(json_data)):
    for ele in range(len(json_data[i]["e"])):
        if json_data[i]["e"][ele]["n"] == "silhouette":
            silhouette.append(json_data[i]["_id"]["$oid"])
        else:
            no_sil.append(i)
    for ele in range(len(json_data[i]["e"])):    
        if json_data[i]["e"][ele]["n"] == "2Dbb":
            object_id.append(json_data[i]["_id"]["$oid"])
            bounding_box.append(json_data[i]["e"][ele]["v"])
            bounding_box_center.append(json_data[i]["e"][ele + 1]["v"])

time_stamp = []

final_list_time_stamp = []
final_list_2D_bb = []
final_list_silhouette = []
final_list_2D_cen = []
my_list_index = []

for i in range(len(json_data) - 1):
    time_stamp.append(json_data[i]["bt"]["$date"])
    my_list_index.append(i)
    if json_data[i]["bt"]["$date"] == json_data[i + 1]["bt"]["$date"]:
        for ele in range(len(json_data[i]["e"]) - 1):
            if json_data[i]["e"][ele]["n"] == "silhouette" and ele == 0:
                final_list_silhouette.append(json_data[i]["e"][ele]["v"])
                final_list_time_stamp.append(json_data[i]["bt"]["$date"])
            else:
                if ele == 0:
                    final_list_silhouette.append(json_data[i + 1]["e"][ele]["v"])
                    final_list_time_stamp.append(json_data[i]["bt"]["$date"])
            if json_data[i]["e"][ele]["n"] == "2Dbb" and ele == 2:
                final_list_2D_bb.append(json_data[i]["e"][ele]["v"])
            else:
                if ele == 2:
                    final_list_2D_bb.append(json_data[i + 1]["e"][ele]["v"])
            if json_data[i]["e"][ele]["n"] == "2DCen" and ele == 3:
                final_list_2D_cen.append(json_data[i]["e"][ele]["v"])
            else:
                if ele == 3:
                    final_list_2D_cen.append(json_data[i + 1]["e"][3]["v"])


#cleaned_time_stamp = []
#for i in time_stamp: 
#    cleaned_time_stamp.append(dateutil.parser.parse(i).replace(tzinfo=None))
#
#cleaned_time_stamp.append(dateutil.parser.parse("3000-12-30T23:00:00.999Z").replace(tzinfo=None))
#numpy_time_stamp = numpy.array(cleaned_time_stamp)
#arr = numpy.diff(numpy_time_stamp)

#print(numpy_time_stamp[:6])
#print(arr[:5])
#print(len(numpy_time_stamp))
#for i, j in enumerate(numpy_time_stamp):
#    if i < 105281 and j == numpy_time_stamp[i + 1]:

for i in range(len(final_list_silhouette)):
    if i < 4:
        print(final_list_time_stamp[i], final_list_silhouette[i])

        
#import numpy
#
#x = numpy.array(no_sil)
#arr = numpy.diff(x)
#for i, e in enumerate(arr):
#    if e == 1:
#        my_list.append(no_sil[i - 1])
