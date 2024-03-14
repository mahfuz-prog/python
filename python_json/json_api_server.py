import os
import json
import csv
from flask import Flask, Response

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/survey_results_100.csv')

data = []
with open(data_file) as f:
	csvReader = csv.DictReader(f)
	for row in csvReader:
		data.append(row)

# serve the data as json string
@app.route('/json-api/')
def json_api():
	response = json.dumps(data, indent=2)
	# json responses
	return Response(response=response, status=200, mimetype='application/json')

if __name__ == '__main__':
	app.run(port=8000)