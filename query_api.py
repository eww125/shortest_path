origin_name = 'olt217'
origin = '38.2169557214312,-85.6787847436338'
destination_name = 'olt219'
destination = '38.2235480822111,-85.6938678122869'

from urllib2 import urlopen
from json import load, dumps
from time import time
t = time()

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
url += '&mode=walkingavoid=highways&key='
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
print "polyline=" + polyline_str

# convert to point
import polyline
polyline_list = polyline.decode(polyline_str)

# write to csv
import pandas as pd
df = pd.DataFrame(polyline_list)
df.columns = ['lat', 'lon']
print df
df.to_csv('data.csv', index=False)

import csv

# Read in raw data from csv
rawData = csv.reader(open('data.csv', 'rb'), dialect='excel')

coordinate_list=[]
# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    if iter >= 2:
        lat = row[0]
        lon = row[1]
        coordinate_list.append("[" + lon + ", " + lat + "]")

final_string = '{"type":"LineString","coordinates":['
final_string += ",".join(str(x) for x in coordinate_list)
final_string += "]}"
print final_string

# opens an geoJSON file to write the output to
outFileHandle = open(origin_name + "_" + destination_name + ".geojson", "w")
outFileHandle.write(final_string)
outFileHandle.close()

print "complete!"
print "Time elapsed: " + str(time() - t) + " s."
