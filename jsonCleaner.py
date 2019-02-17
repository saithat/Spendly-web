import fileinput
import json
import sys

f = open("EmbeddingAPIWorkflowSample/dummyreceipt.json", "r")

datastore = json.load(f)
#datastore = f

print(type(datastore))

count = 0
total = 0.0

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

for i in datastore["recognitionResult"]["lines"]:
    for key, elem in i.items():
        if(count < 4 and count > 0):
            count = count + 1
        if(count == 4):
            if(float(elem)):
                total = float(elem)
                count = count + 1
                break
        if(key == "text"):
            if((count == 0) and (elem == "Total" or elem == "total" or elem == "Total:" or elem == "total:")):
                count = count + 1

print(total)