import json
from flask import Flask, Response
from urllib.request import urlopen

app = Flask(__name__)

# serve the json file on a specific route as response
@app.route('/json-api/')
def json_api():
	with urlopen("http://127.0.0.1:8000/static/survey_results_public.json") as response:
		data = json.load(response)

	# json response
	return Response(response=data, status=200, mimetype='application/json')

if __name__ == '__main__':
	app.run(port=8000)