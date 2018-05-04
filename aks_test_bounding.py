import json

with open('video.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]

final_list_time_stamp = []
final_list_2D_bb = []
final_list_silhouette = []
final_list_2D_cen = []

dict_silhouette = {}
dict_2D_bb = {}
dict_2D_cen = {}

for i in range(len(json_data)):
        if len(json_data[i]["e"]) < 2:
            parsedtimestamp = dateutil.parser.parse(json_data[i]["bt"]["$date"])
            naive = parsedtimestamp.replace(tzinfo=None)
            dict_silhouette[naive] = json_data[i]["e"][0]["v"]
        else :
            parsedtimestamp = dateutil.parser.parse(json_data[i]["bt"]["$date"])
            naive = parsedtimestamp.replace(tzinfo=None)
            dict_2D_bb[naive] = json_data[i]["e"][2]["v"]
            dict_2D_cen[naive] = json_data[i]["e"][3]["v"]

common_keys = set(dict_silhouette.keys()) & set(dict_2D_bb.keys()) & set(dict_2D_cen.keys())

for key in common_keys: 
    final_list_time_stamp.append(key)
    final_list_2D_bb.append(dict_2D_bb[key])
    final_list_silhouette.append(dict_silhouette[key])
    final_list_2D_cen.append(dict_2D_cen[key])