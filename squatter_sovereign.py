#!/usr/bin/env python
import json
import urllib

chronam = 'https://chroniclingamerica.loc.gov'

# Enter Chronicling Ameirca JSON search results url
results = 'https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn82015827&dateFilterType=yearRange&date1=1789&date2=1949&language=&ortext=&andtext=&phrasetext=&proxtext=&proxdistance=5&rows=500&searchType=advanced&format=json'

# Count to keep track of number of files downloaded
count = 0

def get_json(url):
	data = urllib.urlopen(url).read()
	return json.loads(data)

data = get_json(results)

# Cycle through JSON results
for page in data['items']:

	# Create URL
	hit = str(page['id'].encode('utf-8'))
	seed = hit[:-1] + '.pdf'
	download_url = chronam + seed

	# Create File Name
	file_name = download_url.replace('/', '_')
	file_name = file_name[40:]

	# Download and save PDF
	response = urllib.urlopen(download_url)
	file = open(str(file_name), 'wb')
	file.write(response.read())
	file.close()
	print 'file saved: ' + file_name
	count += 1

# Prints number of PDFs downloaded
print str(count) + ' results downloaded'
