import os
import json
with open("./metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
attributlist = []
attributdict = {}
for _data in data: 
    for _attributes in _data['attributes']: 
        attributlist.append(_attributes["value"])
        if _attributes["value"] not in attributdict.keys():
            attributdict[_attributes["value"]] = 0

for _attributdict in attributdict.keys(): 
     attributdict[_attributdict] = 100/len(attributlist) * attributlist.count(_attributdict)

print(attributdict)