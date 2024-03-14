import csv

# used to store rows as dictionary
data = []
# read csv file
with open('survey_results_public.csv') as f:
	csvReader = csv.DictReader(f)

	i = 0
	for row in csvReader:
		# row is a dictionary
		# column name as a key and it's value
		data.append(row)
		print(i, 'Rows done!')

		# we need only 150 rows
		if i == 100:
			break
		i+=1

# create a new csv file with 150 rows
with open('survey_results_100.csv', 'w', newline='') as csvfile:
	# get all the columns name
	# csv.DictWriter required column name
	# send the keys as columns name
	keys = data[0].keys()
	writer = csv.DictWriter(csvfile, fieldnames=keys)

	# Write a row with the field names (as specified in the constructor) to the writer’s file object
	writer.writeheader()
	for item in data:
		writer.writerow(item)