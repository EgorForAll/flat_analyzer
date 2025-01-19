# Функция для формирования строки с информацией о квартире
def format_flat_info(type_flat, area, house_number, floor, flat_number, price):
    return (
        f"Тип квартиры: {type_flat}\n"
        f"Площадь: {area}\n"
        f"Номер дома: {house_number}\n"
        f"Этаж: {floor}\n"
        f"Квартира: {flat_number}\n"
        f"Цена: {price}\n"
    )

# Функция для разделения текста на части
def split_text(text, max_length=4096):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]