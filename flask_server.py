import json
import os
import requests
from flask import Flask
app = Flask(__name__)

token = "n8htaJw8T8g9oByV14pfeMPx43M2CZGhbOePUmek"

@app.route('/return/<food>')
def report(food):
    respList = foodSearch(token, food)
    return respList

def foodSearch(token, query):
    new_query = query

    searchQuery = {"api_key":token, "q":new_query, "format":"JSON", "ds":"Standard Reference"}
    
    searchResponse = requests.get("http://api.nal.usda.gov/ndb/search/", params=searchQuery)

    simpleList = []
    seq = ("name", "ndbno")
    simpleDict = simpleDict.fromkeys(seq)
    responseList = json.loads(searchResponse.text)
    for entry in responseList["list"]["item"]:
        simpleDict["name"] = entry["name"]
        simpleDict["ndbno"] = entry["ndbno"]
        simpleList.append(simpleDict)

    print(simpleList)
    return nutritionalData(simpleList, token)

'''
def nutritionalData(simpleList, token):
    for entry in respList["list"]["item"]:
        reportQuery = {"api_key":token, "ndbno":entry["ndbno"], "type":"b", "format":"json"}
        reportResponse = requests.get("http://api.nal.usda.gov/ndb/reports/", params=reportQuery)
        reportDict = json.loads(reportResponse.text)
        print(json.dumps(reportDict, indent=2))

    return prettyReport
'''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host='0.0.0.0', port=port)
