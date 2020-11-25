#Team 58, Nitika Malhotra (1037082), Anupama Mampage(1102749), Ribhav Shridhar (1037144), Ronak Arvindkumar (1043591)

import json
import couchdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename')
args = parser.parse_args()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Cloud_assignment", timeout=10)


with open(args.filename,encoding="utf8") as rf:
    data = json.load(rf)

SubArea = {}
for i in data["features"]:
    aurin = {}
    aurin["id"] = i["id"]
    lat = i["geometry"]["coordinates"][0][1]
    long = i["geometry"]["coordinates"][0][0]
    loc = str(lat)+", "+str(long)
    location = geolocator.reverse(loc)    
    x = location.address.split("Victoria,",1)[1]
    x = x.split(", Australia",1)[0]
    if x in SubArea:
        SubArea[x]+=1
    else:
        SubArea[x] = 1

with open("subarea_Map", w) as file:
	file.dump(SubArea)
