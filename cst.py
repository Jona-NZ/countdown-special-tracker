from selenium import webdriver
from selenium.webdriver import ChromeOptions
from email.message import EmailMessage
from email.utils import formataddr
from dotenv import load_dotenv
import re
import os
import smtplib
import time


def email(title, full_price, url):
    load_dotenv()
    gUser = os.environ.get('EMAIL_USER')
    gPass = os.environ.get('EMAIL_PASS')

    msg = EmailMessage()
    msg.set_content(
        f'Hello,\n\n{title} is on special at Countdown for {full_price}.\n\nView it here:\n{url}')

    msg['Subject'] = f'{title} is {full_price}'
    msg['From'] = formataddr(('Countdown Specials', os.environ['EMAIL_USER']))
    msg['To'] = [os.environ.get('TO_EMAIL'), '']

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gUser, gPass)
        server.send_message(msg)
        server.close()

        print('Email sent')
    except:
        print('Something went wrong')


def main():
    # Selenium config & run
    options = ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # outdated user agent or VPN can sometimes prevent countdown app from loading product, causing scrape to fail
    url = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=281739'
    stock_code = re.sub("[^0-9]", "", url)

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)

    driver.set_page_load_timeout(250)
    time.sleep(3)

    # Find elements
    try:
        title = driver.find_element_by_xpath(
            '//*[@id="product-details"]/div[2]/h1').text
    except:
        title = 'Countdown Item '

    # Get and format the price
    try:
        uf_price = driver.find_element_by_id(
            f'product-{stock_code}-price').text
        f_price = re.sub("[^0-9]", "", uf_price)

        dollars, cents = f_price[:int(len(f_price)/2)
                                 ], f_price[int(len(f_price)/2):]
        full_price = f'${dollars}.{cents}'
    except:
        print('Error: Unable to find price')
        full_price = ''

    # Get whether the item is on special
    try:
        is_on_special = driver.find_element_by_xpath(
            '//*[@id="product-details"]/div[2]/div[1]/product-price/div/span[2]').text
    except:
        is_on_special = None

    if is_on_special:
        print(f'{title} is on special for {full_price}')
        email(title, full_price, url)
    else:
        print(f'{title} is not on special')

    driver.quit()


if __name__ == '__main__':
    main()
