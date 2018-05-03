import json
from datetime import datetime
import datetime
import dateutil.parser
import pymongo
from matplotlib import pyplot as plt

with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
itemsarray=[]
timearray=[]
videoarrayx=[]
videoarrayy=[]
decodearray=[]
finallist=[]
for i in range(len(json_data)):
    dictless = {}
    id = json_data[i]["_id"]["$oid"]
    uid = json_data[i]["uid"]
    date = json_data[i]["bt"]["$date"]
    items = []
    # if hasattr(json_data[i],"e"):
    for item in json_data[i]["e"]:
        data = {}
        # print("haha")
        # print(item)
        itemsarray.append(data)
        result=dateutil.parser.parse(date)
        naive = result.replace(tzinfo=None)
        print(i)
        times = [[8, 10, 21, 23], [41, 45, 57, 61], [75, 80, 93, 97], [110, 114, 126, 129], [142, 146, 159, 164],
                 [178, 183, 195, 198], [219, 222, 234, 237], [258, 262, 274, 278], [299, 303, 313, 317],
                 [332, 335, 349, 353], [378, 382, 392, 396], [420, 424, 435, 440], [452, 456, 466, 470],
                 [486, 491, 501, 507]]
        timesb = [[8, 10, 21, 25], [36, 39, 53, 56], [68, 72, 86, 91], [99, 102, 118, 122], [134, 138, 151, 155],
                  [168, 173, 190, 192], [210, 212, 230, 235], [249, 252, 269, 272], [281, 283, 302, 306],
                  [317, 320, 339, 342], [357, 360, 373, 377], [391, 394, 410, 413], [426, 429, 443, 446],
                  [456, 459, 471, 474]]
        if naive > datetime.datetime(2018, 3, 22, 17, 27, 56, 0) and naive < datetime.datetime(2018, 3, 22, 17, 36, 46,0):
            for list in times:
                for index in range(len(list)):
                    eventimestamp = datetime.datetime(2018, 3, 22, 17, 27, 56, 0) + datetime.timedelta(0, list[index])
                    checktime = (eventimestamp - naive).total_seconds()
                    # print(checktime)
                    if checktime < 1 and checktime > -1:
                        data["groundtruthstate"] = index
                    flag = index
            if flag == 1:
                data["groundtruthstate"] = 1
            elif flag == 2:
                data["groundtruthstate"] = 2
            elif flag == 0:
                data["groundtruthstate"] = 0
            else:
                data["groundtruthstate"] = 3
            if item["n"] == "silhouette":
                data["id"] = id
                data["type"] = "silhouette"
                data["time"]=naive
                data["imagevalue"] = item["v"]
                import base64
                #encoded = base64.b64encode(data["imagevalue"])
                decode = base64.b64decode(data["imagevalue"])
                data["imagevalue"]=decode
                #decodearray.append(decode)
                finallist.append(data)
            if naive>datetime.datetime(2018, 3, 22, 17, 15, 56, 0) and naive<datetime.datetime(2018, 3, 22, 17,24,2 , 0) :
                for list in timesb:
                    for index in range(len(list)):
                        eventimestamp = datetime.datetime(2018, 3, 22, 17, 15, 56, 0) + datetime.timedelta(0, list[index])
                        checktime=(eventimestamp - naive).total_seconds()
                        #print(checktime)
                        if checktime<1 and checktime >-1:
                            data["groundtruthstate"]=index
                            flag=index

                if flag == 1:
                    data["groundtruthstate"] = 1
                elif flag == 2:
                    data["groundtruthstate"] = 2
                elif flag == 0:
                    data["groundtruthstate"] = 0
                else:
                    data["groundtruthstate"] = 3

                if item["n"] == "silhouette":
                    data["id"] = id
                    data["type"] = "silhouette"
                    data["time"]=naive
                    data["imagevalue"] = item["v"]
                    print(data["imagevalue"])
                    import base64
                    #encoded = base64.b64encode(data["imagevalue"])
                    data["imagevalue"] = base64.b64decode(data["imagevalue"])
                    finallist.append(data)
                    #decodearray.append(decode)
print(finallist)
from PIL import Image

filename = 'silhouette.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(decodearray[2])
img = Image.open(filename)
img.show()


#plt.plot(timearray,videoarrayx)
#plt.plot(timearray,videoarrayy)
#plt.show()
"""
from PIL import Image
# assume data contains your decoded image
filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(decodearray[2])
img = Image.open(filename)
img.show()
"""

"""
        """"""
        else:
            data["id"] = id
            if item["n"] == "frameId":
                data["type"] = "frameId"
                data["frameid"] = item["v"]
            elif item["n"] == "2Dbb":
                data["type"] = "2dboundingbox"
                data["2dbbcoordinates"] = item["v"]
            elif item["n"] == "3Dbb":
                data["type"] = "3dboundingbox"
                data["3dbbcoordinates"] = item["v"]
            elif item["n"] == "3Dcen":
                data["type"] = "3dcentre"
                data["3dcencoordinates"] = item["v"]
            elif item["n"] == "2DCen":
                data["type"] = "2dcentre"
                data["2dcencoordinates"] = item["v"]
                if result > datetime.datetime(2018, 03, 22, 17, 15, 57, 000) and result < datetime.datetime(2018, 03,
                                                                                                            22, 17, 16,
                                                                                                            03, 000):
                    timesec = result.strftime('%H:%M:%S.%f')[:-3]
                    timearray.append(timesec)
                    videoarrayx.append(data["2dcencoordinates"][0])
                    videoarrayy.append(data["2dcencoordinates"][1])
            elif item["n"] == "Activity":
                data["type"] = "Activity"
                data["activity"] = item["v"]
            elif item["n"] == "userID":
                data["type"] = "userID"
                data["userid"] = item["v"]

"""

