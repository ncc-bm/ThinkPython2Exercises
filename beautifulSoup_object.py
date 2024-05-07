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
""" print(type(exampleSoup))

elems = exampleSoup.select('#author')
print(type(elems))      # elems is a list of Tag objects.
print(len(elems))       # the length is 1
print(type(elems[0]))   # <class 'bs4.element.Tag'>
print(str(elems[0]))    # The Tag object as a string. <span id="author"> Al Sweigart</span>
print(elems[0].getText()) # Al Sweigart
print(elems[0].attrs)   # {'id': 'author'} """

""" 
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print()
print(str(pElems[1]))
print(pElems[1].getText())
print()
print(str(pElems[2]))
print(pElems[2].getText())
 """


spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)