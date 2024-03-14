import csv
import json

data = []
with open('survey_results_public.csv') as f:
	csvReader = csv.DictReader(f)
	for row in csvReader:
		data.append(row)

new_string = json.dumps(data, indent=2)

# save json file
with open('survey_results_public.json', 'w') as f:
	json.dump(new_string, f)