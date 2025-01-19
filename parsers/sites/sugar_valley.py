import requests
from bs4 import BeautifulSoup
from utils.helpers import format_flat_info
from config import SUGAR_VALLEY

def parse_sugar_valley():
    response = requests.get(SUGAR_VALLEY)

    soup = BeautifulSoup(response.text, 'html.parser')

    flats = soup.find_all(class_=['item', 'col-12'])

    flats_info = []

    for flat in flats:
        corp_flat_info = get_corp_flat(flat)
        if corp_flat_info is None:
            continue 

        corpus, flat_number = corp_flat_info

        rooms_area_floor_info = get_room_area_floor(flat)
        if rooms_area_floor_info is None:
            continue

        rooms, area, floor = rooms_area_floor_info

        price = get_price(flat)

        if price is None:
            continue

        flats_info.extend(
            (
                format_flat_info(
                    rooms, area, corpus, floor, flat_number, price
                ),
                "-" * 20,
            )
        )
    return flats_info


def get_corp_flat(flat):
    # Ищем блок с информацией о корпусе и квартире
    if elem := flat.find('div', class_='card-header'):
        if info_block := elem.find('div', class_='info'):
            # Извлекаем корпус и номер квартиры
            spans = info_block.find_all('span')
            if len(spans) >= 2:  # Проверяем, что найдены оба элемента
                corpus = spans[0].text.strip()
                flat_number = spans[1].text.strip()
                return corpus, flat_number  # Возвращаем данные, если всё найдено
    
    # Если данные не найдены, возвращаем None
    return None

def get_room_area_floor(flat):
    if info_block := flat.find('div', class_='info mt-3'):
        rooms = info_block.find_all('div', class_='item')[0].text.strip()
        area = info_block.find_all('div', class_='item')[1].text.strip()
        floor_info = info_block.find_all('div', class_='item')[2].text.strip()
        return rooms, area, floor_info
    else:
        return None

def get_price(flat):
    if price_block := flat.find('div', class_='price'):
        if price_span := price_block.find('span', class_='me-2'):
            return price_span.text.strip()
    return None