# 
# Extract the attribute table of a Shp file into a CSV file
#
# @author jeet_sen@yahoo.co.in
# 

import ogr,csv,sys

#Source file
shpfile=r'../work/bbmpwards_old/bbmpwards.shp' #sys.argv[1]
csvfile=r'../work/bbmpwards_old_data.csv' #sys.argv[2]

#Open files
csvfile=open(csvfile,'wb')
ds=ogr.Open(shpfile)
lyr=ds.GetLayer()

#Get field names
dfn=lyr.GetLayerDefn()
nfields=dfn.GetFieldCount()
fields=[]
for i in range(nfields):
    fields.append(dfn.GetFieldDefn(i).GetName())
#Not addding the geometry of the polygon. 
#Uncomment below line to add
#fields.append('kmlgeometry')
csvwriter = csv.DictWriter(csvfile, fields)
try:csvwriter.writeheader() #python 2.7+
except:csvfile.write(','.join(fields)+'\n')

# Write attributes and kml out to csv
for feat in lyr:
    attributes=feat.items()
# Uncomment below to add geometry
#    geom=feat.GetGeometryRef()
#    attributes['kmlgeometry']=geom.ExportToKML()
    csvwriter.writerow(attributes)

#clean up
del csvwriter,lyr,ds
csvfile.close()
