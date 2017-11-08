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
outFileHandle = open("output.geojson", "w")
outFileHandle.write(final_string)
outFileHandle.close()
