from helium import *
from selenium.webdriver import ChromeOptions
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import time
import re
from dotenv import load_dotenv
import os

load_dotenv()

def email():
    gUser = os.environ['EMAIL_USER']
    gPass = os.environ['EMAIL_PASS']

    msg = EmailMessage()
    msg.set_content(f'Hello,\n\n{title} is on special at Countdown for {full_price}.\n\nView it here:\n{url}')

    msg['Subject'] = f'{title} is {full_price}'
    msg['From'] = formataddr(('Countdown Specials', os.environ['EMAIL_USER']))
    msg['To'] = [os.environ['TO_EMAIL'], '']

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gUser, gPass)
        server.send_message(msg)
        server.close()

        print('Email sent')
    except:
        print('Something went wrong')

options = ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')

url = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=281634&name=alpine-cheese-block-edam'
stock_code = re.sub("[^0-9]", "", url)

driver = start_chrome(url, headless=True, options=options)
driver.set_page_load_timeout(15)
time.sleep(3)
driver.save_screenshot("cst_screenshot.png")

#potentialy look at using selenium to get the aria-label for the price

try:
    title = driver.find_element_by_xpath('//*[@id="product-details"]/div[2]/h1').text
except:
    title = 'Countdown Item '

"""
try:
    price2 = driver.find_element_by_id(f'product-{stock_code}-price').text
    print('selenium price: ' + price2)

    prices = find_all(S(f'#product-{stock_code}-price'))
    price = [item.web_element.text for item in prices]
    str_price = re.sub("[^0-9]", "", str(price))

    firstpart, secondpart = str_price[:int(len(str_price)/2)], str_price[int(len(str_price)/2):]

    full_price = f'${firstpart}.{secondpart}'
except:
    print('No price')
    full_price = ''
    """

"""
if Text('Save $').exists():
    print(f'{title} on special for {full_price}')
#    email()
else: print('Item not on special')
"""

if (driver.find_element_by_xpath('//*[@id="product-details"]/div[2]/div[2]/product-price/div/span[2]').text):
    print('Item on special')
else:
    print('Item not on special')


kill_browser()