# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import urllib

# Base URL
chronam = 'https://chroniclingamerica.loc.gov/'

# Chronicling America search results
#results = 'http://chroniclingamerica.loc.gov/search/pages/results/list/?date1=1863&date2=1863&searchType=advanced&language=&proxdistance=5&state=Delaware&rows=500&ortext=&proxtext=&phrasetext=&andtext=&dateFilterType=yearRange&page=1&sort=relevance&format=json'
results_json = 'http://chroniclingamerica.loc.gov/search/pages/results/list/?date1=1863&date2=1863&searchType=advanced&language=&proxdistance=5&state=Delaware&rows=500&ortext=&proxtext=&phrasetext=&andtext=&dateFilterType=yearRange&page=1&sort=relevance&format=json'
# Count to keep track of downloaded files
count = 0

# Record URL Errors
http_errors = []

# Gets search results in JSON format
#results_json = results + '&format=json'

# Returns JSON 
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))
    
data = get_json(results_json)

# Cycle through JSON results
for page in data['items']:
    # Create URL
    hit = str(page['id'])
    seed = hit + 'ocr.txt'
    download_url = chronam + seed
 
    # Create file name
    file_name = download_url.replace('/', '_')
    file_name = file_name[41:]
    
    # Download .txt of the page
    try:
        urllib.request.urlretrieve(download_url, str(file_name))
        print ('file saved: ' + file_name)
        count += 1
    except urllib.error.HTTPError as err:
        http_errors.append('ERROR: ' + str(err.code) + ' ' + str(file_name))
        #print(err.code)

print (str(count) + ' results downloaded') 
for i in http_errors:
    print (i)
