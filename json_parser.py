import json
from pprint import pprint

f = open('directions_api_response.json', 'r')
parsed_json = json.loads(f.read())
f.close()

#pprint(parsed_json['routes'][0]['legs'][0]['steps'])
#overview_polyline
test = parsed_json['routes'][0]['overview_polyline']
print test.items()[0][1]

with open("polyline.txt", "w") as text_file:
    text_file.write(test.items()[0][1])
