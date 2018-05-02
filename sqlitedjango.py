dictionarystore = {}
with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
print(len(json_data))
"""
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