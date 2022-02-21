from helium import *
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()
#options.add_argument("window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

url='https://shop.countdown.co.nz/shop/productdetails?stockcode=281911&name=mainland-edam-cheese-mild-creamy'
s_url = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=281739&name=mainland-organic-cheddar-cheese-100-organic-milk'

start_chrome(s_url, headless=True, options=options)

if Text('Save $').exists():
    print('Item on special')
else: print('Item not on special')

kill_browser()