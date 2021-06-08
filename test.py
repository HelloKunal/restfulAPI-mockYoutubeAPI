import requests
# this lets send post, get requests etc

BASE = "http://127.0.0.1:5000/"

# put gives data in form of json
response = requests.put (BASE + "video/1", {"likes" : 10})
print (response.json())