#Team 58, Nitika Malhotra (1037082), Anupama Mampage(1102749), Ribhav Shridhar (1037144), Ronak Arvindkumar (1043591)

import json
import couchdb
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Cloud_assignment", timeout=10)

couch = couchdb.Server("http://admin:admin@172.26.134.24:5984/")
db = couch["aurin_traffic_new"]

with open('aurin_EnvironmentData.json',encoding="utf8") as rf:
    data = json.load(rf)

for i in data["features"]:
    aurin = {}
    aurin["id"] = i["id"]
    aurin["lat"] = i["properties"]["lattitude"]
    aurin["long"] = i["properties"]["longitude"]
    aurin["GreenSpaceName"] = i["properties"]["name"]
    aurin["_id"] = aurin["id"]
    db.save(aurin)