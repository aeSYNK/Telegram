import json

data = open("news.json")
parser = json.load(data)
for i in parser:
    print(i)
data.close()