import requests
import time
from bs4 import BeautifulSoup


def extractOne(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transformOne(soup):

    try:
        specialVerifier = soup.find(
            'span', class_='price price--was ng-star-inserted').text.strip()
    except:
        specialVerifier = 'Not on special'

    job = {specialVerifier}
    print(job)


def main():
    print('Checking if item is on special...')
    url = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=102323&name=remedy-organic-kombucha-mango-passionfruit'
    transformOne(extractOne(url))


main()
