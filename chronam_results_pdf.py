#!/usr/bin/env python
import json
import urllib.request


chronam = 'https://chroniclingamerica.loc.gov'
# Enter Chronicling Ameirca search results url
results = 'https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=yearRange&date1=1963&date2=1963&language=&ortext=&andtext=&phrasetext=Mona+Lisa&proxtext=&proxdistance=5&rows=20&searchType=advanced'

# Count to keep track of number of files downloaded
count = 0

# Creates JSON file of search results
results_json = results + '&format=json'
#print(results_json)

def get_json(url):
    #data = urllib.urlopen(url).read()
    data = urllib.request.urlopen(results_json).read()
    output = json.loads(data)
    return output

output = get_json(results_json)

#print (output)

# Cycle through JSON results
for page in output['items']:
    
    # Create URL
    hit = str(page['id'].encode('utf-8'))
    seed = hit[2:-2] + '.pdf'
    download_url = chronam + seed

    # Create File Name
    file_name = download_url.replace('/', '_')
    file_name = file_name[40:]

    # Download and save PDF 
    urllib.request.urlretrieve(download_url, str(file_name))
    print('file saved: ' + file_name)
    count += 1

# Prints number of PDFs downloaded
print (str(count) + ' results downloaded')
