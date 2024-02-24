import json
import requests

# request to out json api
r = requests.get('http://127.0.0.1:8000/json-api/')
data = r.json()

# create a new list of dictionary
modified_list = []
for row in data:
    # exclude the row for RemoteWork & ConvertedCompYearly's Null value
    if row['RemoteWork'] == 'NA' or row['ConvertedCompYearly'] == 'NA':
        pass
    else:
        # append modified dictionay to the list
        modified_list.append({'RemoteWork':row['RemoteWork'], 'YearsCode':row['YearsCode'], 
            'Age':row['Age'], 'WebframeHaveWorkedWith':row['WebframeHaveWorkedWith'], 
            'ConvertedCompYearly':row['ConvertedCompYearly']})

# dump the modified list
string = json.dumps(modified_list, indent=2)

print(string)