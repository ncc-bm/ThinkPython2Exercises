#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...')           # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'pypi.org ' + ' '.join(sys.argv[1:]))

#webbrowser.open('https://google.com/search?q=' 'pypi.org ' + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as excp:
    print('There was a problem %s' % (excp))

# Retrive top search  result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('a', jsname='UWckNb')
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
