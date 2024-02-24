import csv
import json

# read csv file
with open('survey_results_public.csv', encoding='utf-8') as f:
	csvReader = csv.DictReader(f)

	data = []
	for row in csvReader:
		data.append(row)
		print(row['ResponseId'], 'Rows done!')

new_string = json.dumps(data, indent=2)

# save json file
with open('static/survey_results_public.json', 'w') as f:
	json.dump(new_string, f)