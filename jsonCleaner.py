import fileinput
import json
import sys
import array
import datetime
from geopy.geocoders import MapBox
import mapbox_creds

f = open("EmbeddingAPIWorkflowSample/dummyreceipt.json", "r")

datastore = json.load(f)
#datastore = f

arr = [["Kroger", "Publix", "Walmart", "Whole Foods", "Aldi", "Sprouts"],["McDonald's", "Wendy's", "Frisch's Big Boy", "OMG! Rotisserie", "Domino's Pizza", "Long John Silver's", "Whataburger", "Hamburger King", "Burger King"], ["Mapco", "Pilot", "Shell", "BP", "Exxon"]]

print(type(datastore))

count = 0
total = 0.0
typ = ""
dat = ""

'''for recognitionResult in datastore:
    for lines in recognitionResult.items():
        for text in lines.items():
            if(count == 1):
                if(float(text)):
                    total = float(text)
                    count = count + 1
                    break
            if((count == 0) and (text == "Total" or text == "total" or text == "Total:" or text == "total:")):
                count = count + 1
'''
clean = []

for i in datastore["recognitionResult"]["lines"]:
    for key in i:
        if(key == "text"):
            clean.append(i[key])

print(clean)

try:
    tmp = clean.index("Total")
    print(tmp)
    total = float(clean[tmp+1])
except (RuntimeError, TypeError, NameError):
    try:
        tmp = clean.index('Total:')
        total = float(clean[tmp+1])
    except (RuntimeError, TypeError, NameError):
        print("Error finding Total")

for i in range(10):
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if((arr[j][k]) == clean[i]):
                if(j == 0):
                    typ = "Groceries"
                elif j == 1:
                    typ = "Fastfood"
                elif j == 2:
                    typ = "Gas"
                else:
                    typ = "Other"

dat = datetime.datetime.now()

geolocator = MapBox(api_key=mapbox_creds.API_KEY,user_agent="spendly-web")
location = geolocator.geocode(clean[2]+ clean[3])
timey = dat.strftime('{%Y-%m-%d.%H:%M:%S}')

data = { 
    'timestamp': timey, 
    'latitude': location.latitude, 
    'longitude': location.longitude,
    "cost": total, 
    'type': typ
}

fname = "test.json"

with open(fname, 'w') as s:
    json.dump(data, s)
