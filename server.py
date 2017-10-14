from flask import Flask, request, render_template, url_for
import json
app = Flask(__name__)
import keys
import urllib2
from ingredient_parser.en import parse
import requests
import urllib

userChoices = []
userIngredients = []

@app.route("/getUserChoices")
def getChoices():
	return str(userChoices)

@app.route('/getIngredients')
def getIngredients():
	return str(userIngredients)

@app.route('/getFood', methods=['POST'])
def getFood():
	s = "https://api.edamam.com/search?q="
	s+= str(request.form['food']).replace(" ", "%20") + "&app_id=" + keys.appID() + "&app_key=" + keys.appSecret()
	print s
	webUrl  = urllib2.Request(url = s)
	webUrl = urllib2.urlopen(webUrl)
	if(webUrl.getcode() == 200):
		results = []
		counter = 0
		response = webUrl.read().decode('utf-8')
		theJSON = json.loads(response)
		for i in range(0, len(theJSON['hits'][0]['recipe']['ingredients'])):
			results.append(parse(theJSON['hits'][0]['recipe']['ingredients'][i]['text'])['name'])
		url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"
		postReq = []
		counter = 0
		for i in range(0, len(results)):
			postReq.append({"language": "en", "id": str(counter), "text": results[i].encode('utf-8')})
			counter+=1
		payload = str({"documents": postReq})
		headers = {
    	'content-type': "application/json",
    	'ocp-apim-subscription-key': str(keys.azureKey())
    	}
		print payload
		response = requests.request("POST", url, data=payload, headers=headers)
		response = response.json()
		print response
		for i in range(0, len(response['documents'])):
			userIngredients.append(parse(response['documents'][i]['keyPhrases'][0])['name'])
		userChoices.append(theJSON['hits'][0])
		return str(theJSON['hits'][0]['recipe']['label'])


app.run(debug=True)
