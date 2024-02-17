import json

with open("sample-data.json", "r") as file:
    data = json.load(file)
    for el in data['imdata']:
        print(el['l1PhysIf']['attributes']['dn'],
              el['l1PhysIf']['attributes']['speed'],
              el['l1PhysIf']['attributes']['mtu'],
              sep="  ")
