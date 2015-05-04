import sys, argparse, csv
from pygeocoder import Geocoder

# Command arguments
parser = argparse.ArgumentParser(description='Geocode from CSV')
parser.add_argument('file', help='csv file to read', action='store')
args = parser.parse_args()
csv_file = args.file

# Open Output file
outfile = csv.writer(open("out.csv", "wb"))

# Open CSV file
with open(csv_file, 'rb') as csvfile:
   count = 0
   # get number of columns
   for line in csvfile.readlines():
     count += 1
     array = line.split(",")
     state_item = array[1]
     city_item  = array[3]
     location = city_item + "," + state_item
     print(count)
     print(location) 
     results = Geocoder.geocode(location)
     #`print(results[0].coordinates)
     latitude = str(results[0].latitude)
     longitude = str(results[0].longitude)
     array.extend([latitude,longitude])
     outfile.writerow(array)
close(outfile)
