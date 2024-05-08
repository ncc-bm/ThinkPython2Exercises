import requests, webbrowser, bs4, os

nbu_exchange_rate_url = 'https://nbu.uz/uz/exchange-rates/'

def get_nbu_exchange_rate(url):
    web_page = requests.get(url)
    try:
        web_page.raise_for_status()
    except Exception as excpt:
        print('There is a problem with %s' %(excpt))
    soup = bs4.BeautifulSoup(web_page.text, 'lxml')
    exchange_table = soup.select('.kursdata')
    
    return exchange_table[1]

""" web_page = requests.get(nbu_exchange_rate_url)
try:
    web_page.raise_for_status()
except Exception as excpt:
    print('There is a problem with %s' % (excpt))

soup = bs4.BeautifulSoup(web_page.text, 'lxml')
exchange_table = soup.select('.kursdata')
 """

exchange_rate_file = open('exchange.html', 'w')
exchange_rate_file.write('<html><body>')

exchange_rate_file.write('<h1>NBU Exchange Rate</h1>')
exchange_rate_file.write(str(get_nbu_exchange_rate(nbu_exchange_rate_url)))

exchange_rate_file.write('</body></html>')


webbrowser.open('file://'+ os.path.join(os.path.abspath('.'), exchange_rate_file.name))

