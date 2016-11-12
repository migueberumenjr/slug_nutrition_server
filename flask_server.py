import json
import os
import requests
from flask import Flask
app = Flask(__name__)

token = "mTT5GDs1I6azjuW2U8dm1hHsmtfFPxjRoZvzbibl"

@app.route('/return/<food>')
def report(food):
    respList = foodSearch(token, food)
    return respList

def foodSearch(token, query):
    searchQuery = {"api_key":token, "q":query, "format":"JSON", "ds":"Standard Reference"}
    
    searchResponse = requests.get("http://api.nal.usda.gov/ndb/search/", params=searchQuery)

    simpleList = []
    seq = ("name", "ndbno")
    responseList = json.loads(searchResponse.text)
    for entry in responseList["list"]["item"]:
        simpleDict = {}
        simpleDict = simpleDict.fromkeys(seq)
        simpleDict["name"] = entry["name"]
        simpleDict["ndbno"] = entry["ndbno"]
        simpleList.append(simpleDict)

    print(simpleList)
    return json.dumps(simpleList)
'''
def nutritionalData(simpleList, token):
    for entry in respList["list"]["item"]:
        reportQuery = {"api_key":token, "ndbno":entry["ndbno"], "type":"b", "format":"json"}
        reportResponse = requests.get("http://api.nal.usda.gov/ndb/reports/", params=reportQuery)
        reportDict = json.loads(reportResponse.text)
        print(json.dumps(reportDict, indent=2))

    return prettyReport
    
    return("Hello")
'''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host='0.0.0.0', port=port)
