import requests

BASE = "http://127.0.0.1:5000/"

data =[
    {"likes":100, "name": "Movie1", "views": 10000},
    {"likes":20, "name": "Movie2", "views": 100000},
    {"likes":0, "name": "Movie3", "views": 10000},
]

for i in range(len(data)): 
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input("Press Enter")

response = requests.get(BASE + "video/6")
print(response.json())