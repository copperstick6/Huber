'use strict';

const ApiAiApp = require('actions-on-google').ApiAiApp

var request = require('request');
const WELCOME_INTENT = 'input.welcome'; //this is the name rom the API.AI intent. check the API.AI event console.
const FOOD_INTENT = 'input.food';

exports.huber = (req, res) => {
  const app = new ApiAiApp({ request: req, response: res});
  function welcomeIntent(app){
    app.ask('Welcome to Hueber. Say any food item and we\'ll order ingredients right to your doorstep.')
  }
  function getFood(app){
	  let foodItem = app.data.food
	  var options = { method: 'POST',
  	url: 'http://1094eb34.ngrok.io/getFood',
	  headers:
   	{ 'postman-token': '5c132ad5-e841-c625-1002-0484dfe5f1ca',
     'cache-control': 'no-cache',
     	'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' },
  	formData: { food: String(foodItem) } };

	request(options, function (error, response, body) {
		let arr = String(body).split(',')
		app.tell("Got your food request! We got a sweet recipe for " + arr[0] + "! We'd also like to recommend " + arr[1] + " and " + arr[2] + ". Check out your order status via your app!")
	});
  }
  let actionMap = new Map();
  actionMap.set(WELCOME_INTENT, welcomeIntent)
  actionMap.set(FOOD_INTENT, getFood)
  app.handleRequest(actionMap);
}
