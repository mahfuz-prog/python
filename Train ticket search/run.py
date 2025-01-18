import requests
from requests_html import HTMLSession, HTML


def get_result(data):
	html = HTML(html=data)
	name = html.find('.trip-name', first=True).text
	seat_status = html.find('.seat-classes-row .all-seats')

	# for item in seat_status:
	# 	if item.text != '0':
	# 		return True
	# 	else:
	# 		return False

	if seat_status[-1].text != '0':
		return True
	else:
		return False

	available_seat = html.find('.available-text')[-1].text
	journey_start = html.find('.journey-start', first=True).text


def proxy(url):
	user = ''
	password = ''

	payload = {'source': 'universal', 'url': url, 'geo_location': 'United States', "render": "html"}

	response = requests.request(
	    'POST',
	    'https://realtime.oxylabs.io/v1/queries',
	    auth=(user, password),
	    json=payload,
	)
 
	return response.json()['results'][0]['content']



start_range = ['Khulna', 'Noapara', 'Jashore', 'Mubarakganj', 'Kotchandpur', 'Darshana_Halt']
end_range = ['Birampur', 'Fulbari', 'Parbatipur', 'Saidpur', 'Nilphamari', 'Domar', 'Chilahati']


for start in start_range:
	for end in end_range:
		print(f'Searching for {start} to {end} ...')
		from_station = start
		to_station = end
		date = '11-Jun-2024'
		url = f'https://eticket.railway.gov.bd/booking/train/search?fromcity={from_station}&tocity={to_station}&doj={date}&class=S_CHAIR'

		data = proxy(url)
		html = HTML(html=data)

		items = html.find('app-single-trip')
		for item in items:
			status = get_result(item.html)
			if status:
				print('================')
				print(item.text)
				print()