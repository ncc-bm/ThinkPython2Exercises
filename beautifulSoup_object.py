import requests, bs4

""" res = requests.get('https://nostarch.com')

try:
    res.raise_for_status()
except Exception as excp:
    print('There was a problem %s' % (excp))
    
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))
 """

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'lxml')
print(type(exampleSoup))