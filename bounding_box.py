import json
import dateutil
import numpy

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
