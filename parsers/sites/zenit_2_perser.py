import requests
from bs4 import BeautifulSoup
from utils.helpers import format_flat_info
from config import ZENIT_2

def parse_zenit():
    # Загрузка страницы
    response = requests.get(ZENIT_2)
    soup = BeautifulSoup(response.text, 'html.parser')

    flats = soup.find_all(class_=['item'])

    filtered_flats = [flat for flat in flats if 'lock' not in flat.get('class', [])]

    # Список для хранения информации о квартирах
    flats_info = []

    # Извлечение данных
    for flat in filtered_flats:
        if info_flat := flat.find('div', class_='info-flat'):
            # Тип квартиры и площадь
            title = info_flat.find('h3', class_='title').text.strip()
            type_flat, area = title.split(' - ')  # Разделяем на тип квартиры и площадь

            # Номер дома, этаж и квартира
            primary_title = info_flat.find('div', class_='primary-title').text.strip()
            parts = primary_title.split(',')  # Разделяем на части
            house_number = parts[0].strip()  # Дом №9
            floor = parts[1].strip()  # этаж 3
            flat_number = parts[2].strip()  # кв 24
            price = get_price(flat)

            # Форматируем информацию о квартире и добавляем в список
            flats_info.extend(
                (
                    format_flat_info(
                        type_flat, area, house_number, floor, flat_number, price
                    ),
                    "-" * 20,
                )
            )

    total = f'Доступны для покупки: {len(filtered_flats)}'

    flats_info.append(total)

    return flats_info


def get_price(flat):
    # Ищем блок с ценой
    price_block = flat.find('div', class_='price')

    if price_block:
        # Извлекаем цену из <h3>
        return price_block.find('h3', class_='h3').text.strip()
    else:
        return "не найдена"