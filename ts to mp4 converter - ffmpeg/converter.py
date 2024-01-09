import os
import time
import subprocess

def ts_to_mp4(ts_list):
	for ts in ts_list:
		print()
		mp4_title = ts.replace('.ts', '.mp4')
		print(ts, ', converting to .mp4...')
		# convert to .mp4
		subprocess.run(['ffmpeg', '-i', ts, mp4_title], shell=True)
		os.remove(ts)
		print()
		print('Program sleeping for 2 minutes.....')
		# to reduce cpu pressure
		time.sleep(120)

# Rename the title and change the order number
def rename(title, i):
	title = title.split('-')
	title[0] = i
	title = ' '.join([str(elem) for elem in title])
	return title


# put all the section inside videos folder
os.chdir('videos3')
for section in os.listdir():
	print('section', section)
	os.chdir(section)
	ts_list = []
	i = 1
	for video in os.listdir():

		# run this function once to rename title
		# while runing this function comment ts_to_mp4 function
		#title = rename(video, i)
		#print(title)
		#os.rename(video, title)
		ts_list.append(video)
		i+=1

        # uncomment after rename title and run the app again
	ts_to_mp4(ts_list)
	ts_list = []
	print()
	os.chdir('..')

print('All videos converted')
