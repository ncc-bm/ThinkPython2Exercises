import requests, webbrowser, bs4, os

nbu_exchange_rate_url = 'https://nbu.uz/uz/exchange-rates/'
aloqabank_exchange_rate_url = 'https://aloqabank.uz/ru/services/exchange-rates/'
kapital_bank_exchange_rate_url = 'https://www.kapitalbank.uz/ru/services/exchange-rates/'


def get_nbu_exchange_rate(url):
    web_page = requests.get(url)
    try:
        web_page.raise_for_status()
    except Exception as excpt:
        print('There is a problem with %s' %(excpt))
    soup = bs4.BeautifulSoup(web_page.text, 'lxml')
    exchange_table = soup.select('.kursdata')
    
    return exchange_table[1]

def get_aloqabank_exchange_rate(url):
    web_page = requests.get(url)
    try:
        web_page.raise_for_status()
    except Exception as excpt:
        print('There is a problem with %s' % (excpt))

    soup = bs4.BeautifulSoup(web_page.text, 'lxml')
    exchange_table = soup.select('div[data-tabs-target="tab2"] table')

    return exchange_table[0]

def get_kapitalbank_exchange_rate(url):
    web_page = requests.get(url)
    try:
        web_page.raise_for_status()
    except Exception as excpt:
        print('There is a problem with %s' % (excpt))

    soup = bs4.BeautifulSoup(web_page.text, 'lxml')
    exchange_table = soup.select('#kb-currency-rates-data')

    return exchange_table

""" 
exchange_rate_file = open('exchange.html', 'w')
exchange_rate_file.write('<html><body>')

exchange_rate_file.write('<h1>NBU Exchange Rate</h1>')
exchange_rate_file.write(str(get_nbu_exchange_rate(nbu_exchange_rate_url)))

exchange_rate_file.write('<br>')
exchange_rate_file.write('<h1>Aloqabank Exchange Rate</h1>')
exchange_rate_file.write(str(get_aloqabank_exchange_rate(aloqabank_exchange_rate_url)))

exchange_rate_file.write('</body></html>')


webbrowser.open('file://'+ os.path.join(os.path.abspath('.'), exchange_rate_file.name))

 """
print(get_kapitalbank_exchange_rate(kapital_bank_exchange_rate_url))