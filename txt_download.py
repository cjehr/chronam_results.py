# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import urllib

# Base URL
chronam = 'https://chroniclingamerica.loc.gov/'

# Chronicling America search results
results = 'https://chroniclingamerica.loc.gov/search/pages/results/?state=Alaska&dateFilterType=yearRange&date1=1789&date2=1963&language=&ortext=&andtext=cleveland&phrasetext=&proxtext=&proxdistance=5&rows=20&searchType=advanced'

# Count to keep track of downloaded files
count = 0

# Gets search results in JSON format
results_json = results + '&format=json'

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
    urllib.request.urlretrieve(download_url, str(file_name))
    print ('file saved: ' + file_name)
    count += 1
    

print (str(count) + ' results downloaded')    
