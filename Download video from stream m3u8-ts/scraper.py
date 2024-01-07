import os
import m3u8
import time
import json
import random
from requests_html import HTMLSession
from urllib.parse import urlparse

session = HTMLSession()

# this function used to seperate title, section, url of current page video
# save into a json file
def save_info(page_url):
	vid_info = {}
	i = 1
	url = page_url
	while True:
		url_parse = urlparse(url)
		path = url_parse.path.split('/')
		vid_title, vid_section, vid_url = path[-1], path[-2], video_url(url)
		print(i, vid_title)
		time.sleep(sleeper())
		vid_info.update({i : {'title': vid_title, 'section': vid_section, 'url' : vid_url}})

		#check the last video
		if 'end-part-1' in url:
			print('All videos found!')
			break
		url = next_url(url)
		i+=1

	# save the data in json file
	obj = json.dumps(vid_info, indent=2)
	with open('info.json', 'w') as f:
		f.write(obj)


# extract stream url from given url
def video_url(url):
	response = session.get(url)
	video = response.html.find('.relative.m-auto.flex.my-2.w-full mux-player', first=True) 
	return f"https://stream.mux.com/{video.attrs['playback-id']}.m3u8?redundant_streams=true"


# used request to server different time
def sleeper():
	time_sleep = [.01,.02,.03,.04]
	random.shuffle(time_sleep)
	return time_sleep[0]

# this function return next page url
def next_url(url):
	response = session.get(url)
	next_page = response.html.find('.flex.items-center.justify-between a')
	for page in next_page:
		if page.text == 'Next lesson':
			return str(page.absolute_links)[2:-2]

# load data from saved json file
def load_info():
	with open('info.json', 'r') as f:
		data = json.load(f)
		return data

# return the uri with specific resolution
def playlist_info(uri):
	r = session.get(uri)
	time.sleep(sleeper())
	obj = m3u8.loads(r.text)

	# extract info from m3u8 object
	print()
	print('Video resolution', obj.data['playlists'][4]['stream_info']['resolution'])
	return obj.data['playlists'][4]['uri']

# save multiple transport stream(ts) file into one ts file
# request on a specific resolution uri it returns a obj with 
# multiple ts files and m3u8 keep track on ts
def save_ts(uri, section, vid_title):
	r = session.get(uri)
	time.sleep(sleeper())
	obj = m3u8.loads(r.text)
	os.chdir(section)
	ts_file_name = f'{vid_title}.ts'

	print(f'Downloading {vid_title}')
	with open(ts_file_name, 'wb') as f:
		i = 1
		for segment in obj.data['segments']:
			h = segment['uri']
			r = session.get(h)
			f.write(r.content)
			print(f'{i} ts done of {vid_title}')
			i+=1

	os.chdir("..")
	return True

# iterate all the data from loaded data from json file
def start_scraping(vid_info):
	i = 1
	for info in vid_info:
		vid_title, vid_section, vid_url = vid_info[info]['title'], vid_info[info]['section'], vid_info[info]['url']

		# adding divergent series first maintan the order of video
		vid_title = f'{i}-{vid_title}'

		# create non existing section
		if not vid_section in os.listdir():
			os.mkdir(vid_section)
			print(f'{vid_section} folder added')
			print()

		uri = playlist_info(vid_url)
		save_ts(uri, vid_section, vid_title)

		print(f'total {i} ts downloaded')
		print()
		i+=1

# first video page
url = 'https://updraft.cyfrin.io/courses/security/smart-contract-security-introduction/trailer'

# Run this function to save all information
# save_info(url)

vid_info = load_info()

# total number of video info loaded
print(len(vid_info))
start_scraping(vid_info)
