from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
#    elem = browser.find_element_by_class_name(' cover-thumb')
    elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
print(type(linkElem))

linkElem.click()

browser.get('https://login.metafilter.com')
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('you_real_user_name_here')

passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('you_real_password_here')
#passwordElem.submit()