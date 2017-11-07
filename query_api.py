origin_name = 'olt213'
origin = '38.21111009024,-85.6749767640669'
destination_name = 'olt214'
destination = '38.2095914883332,-85.6879256717424'

from urllib2 import urlopen
from json import load, dumps

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'google_maps_directions_api', 'r')
API_KEY = f.read().rstrip()
f.close()
print "API_KEY=" + API_KEY

#build the url
url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
url += origin
url += '&destination='
url += destination
url += '&key='
url += API_KEY
print "url=" + url

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

# extract overview_polyline from json
polyline_dict = json_obj['routes'][0]['overview_polyline']
polyline_str = (polyline_dict.items()[0][1]).decode("utf-8")

# convert to point
import polyline
print len(polyline.decode(polyline_str))
