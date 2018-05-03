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
        result = result.replace(tzinfo=None)
        print(i)

        if item["n"] == "silhouette":
            data["id"] = id
            data["type"] = "silhouette"
            data["imagevalue"] = item["v"]
            print(data["imagevalue"])
            import base64
            #encoded = base64.b64encode(data["imagevalue"])
            decode = base64.b64decode(data["imagevalue"])
            decodearray.append(decode)

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

