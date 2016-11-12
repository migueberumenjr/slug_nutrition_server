import json
import os
import requests
from flask import Flask
app = Flask(__name__)

token = "n8htaJw8T8g9oByV14pfeMPx43M2CZGhbOePUmek"

@app.route('/return/<food>')
def report(food):
    #return 'Hello, %s!' % food
    respList = foodSearch(token, food)
    return respList

def foodSearch(token, query):
    new_query = "raw " + query

    searchQuery = {"api_key":token, "q":new_query, "format":"JSON", "ds":"Standard Reference"}
    
    searchResponse = requests.get("http://api.nal.usda.gov/ndb/search/", params=searchQuery)
    responseList = json.loads(searchResponse.text)
    return nutritionalData(responseList, token)

def nutritionalData(respList, token):
    '''
    for entry in respList["list"]["item"]:
        reportQuery = {"api_key":token, "ndbno":entry["ndbno"], "type":"b", "format":"json"}
        reportResponse = requests.get("http://api.nal.usda.gov/ndb/reports/", params=reportQuery)
        reportDict = json.loads(reportResponse.text)
        print(json.dumps(reportDict, indent=2))
    '''
    print(respList["list"]["item"][0]["ndbno"])
    reportQuery = {"api_key":token, "ndbno":respList["list"]["item"][0]["ndbno"], "type":"b", "format":"json"}
    reportResponse = requests.get("http://api.nal.usda.gov/ndb/reports/", params=reportQuery)
    reportDict = json.loads(reportResponse.text)
    prettyReport = json.dumps(reportDict, indent=2)
    print(prettyReport)

    return prettyReport

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host='0.0.0.0', port=port)
