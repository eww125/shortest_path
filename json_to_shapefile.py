import json

myArray = []
with open('my.json') as json_data:
    d = json.load(json_data)
    #print(d)
    myArray.append(d)

print len(myArray[0])
