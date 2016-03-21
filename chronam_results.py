#!/usr/bin/env python
import json
import urllib


chronam = 'http://chroniclingamerica.loc.gov'
# Enter Chronicling Ameirca search results url
results = 'http://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=yearRange&date1=1836&date2=1922&language=&ortext=&andtext=&phrasetext=batman&proxtext=&proxdistance=5&rows=20&searchType=advanced'

# Count to keep track of number of files downloaded
count = 0

# Creates JSON file of search results
results_json = results + '&format=json'

def get_json(url):
	data = urllib.urlopen(url).read()
	return json.loads(data)

data = get_json(results_json)

# Cycle through JSON results
for page in data['items']:
	
	# Create URL
	hit = str(page['id'].encode('utf-8'))
	seed = hit[:-1] + '.pdf'
	download_url = chronam + seed
	
	# Create File Name
	file_name = download_url.replace('/', '_')
	file_name = file_name[39:] 

	# Download and save PDF 
	response = urllib.urlopen(download_url)
	file = open(str(file_name), 'wb')
	file.write(response.read())
	file.close()
	print 'file saved: ' + file_name
	count += 1

# Prints number of PDFs downloaded
print str(count) + ' results downloaded'
