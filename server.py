from flask import Flask, request, render_template, url_for, current_app, make_response
from datetime import timedelta
import json
app = Flask(__name__)
import keys
import urllib2
from ingredient_parser.en import parse
import requests
import urllib
import itemSorter
import random
from flask_cors import CORS
from functools import update_wrapper

userChoices = []
userIngredients = []
randomList = []

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route("/getUserChoices")
@crossdomain(origin='*')
def getChoices():
	return str(userChoices)

@app.route('/randomRecipe')
@crossdomain(origin='*')
def getRandom():
	if(len(randomList) > 0):
		print random.choice(randomList)
		return str(random.choice(randomList)).encode('utf-8')
	else:
		s = "https://api.edamam.com/search?q=Italian"
		s+= "&app_id=" + keys.appID() + "&app_key=" + keys.appSecret()
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
			response = requests.request("POST", url, data=payload, headers=headers)
			response = response.json()
			for i in range(0, len(response['documents'])):
				userIngredients.append(parse(response['documents'][i]['keyPhrases'][0])['name'])
			userChoices.append(theJSON['hits'][0])
			randomList.append(theJSON['hits'][1])
			randomList.append(theJSON['hits'][2])
			return theJSON['hits'][0]
@app.route('/getIngredients')
@crossdomain(origin='*')
def getIngredients():
	return str(userIngredients)

@app.route('/similaritems')
@crossdomain(origin='*')
def getSims():
	itemSorter.readItems()
	itemSorter.readProducts()
	itemSorter.popularItems()
	return str(itemSorter.getSimilarItem(userIngredients))

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
		response = requests.request("POST", url, data=payload, headers=headers)
		response = response.json()
		for i in range(0, len(response['documents'])):
			userIngredients.append(parse(response['documents'][i]['keyPhrases'][0])['name'])
		userChoices.append(theJSON['hits'][0])
		randomList.append(theJSON['hits'][1])
		randomList.append(theJSON['hits'][2])
		return theJSON['hits'][0]['recipe']['label'].encode('utf-8') + ", " + theJSON['hits'][1]['recipe']['label'].encode('utf-8') + ", " + theJSON['hits'][2]['recipe']['label'].encode('utf-8')



app.run(debug=True)
CORS(app)
