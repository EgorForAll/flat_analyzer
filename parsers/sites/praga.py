import requests
from bs4 import BeautifulSoup
from config import PRAGA
from utils.helpers import format_flat_info

def parse_praga():
    response = requests.get(PRAGA)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price = get_price(soup)
    
    return format_flat_info("3", "91", "", "3 собственных этажа", "", price)
    
    

def get_price(soup):
    if price_tag := soup.find('span', {'itemprop': 'price'}):
        return price_tag.text.strip().replace('\xa0', ' ')
    else:
        return "Цена не найдена"