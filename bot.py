from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN
from parsers.sites.zenit_2_perser import parse_zenit
from parsers.sites.sugar_valley import parse_sugar_valley
from parsers.website_parser import parse_website
from parsers.sites.praga import parse_praga
from utils.helpers import split_text

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот для отслеживания информации по интересующим вас застройщикам.')

# Команда /check
async def check_zenit(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Информация по Зенит-2: \n \n")

    flats_info = await parse_website(parse_zenit)

    # Объединяем информацию о квартирах в одну строку
    all_info = "\n".join(flats_info)

    # Разделяем текст на части
    text_parts = split_text(all_info)

    for part in text_parts:
        await update.message.reply_text(part)
        
    
async def check_sugar_valley(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Информация по ЖК Сахарный Дол: \n \n")

    flats_info = await parse_website(parse_sugar_valley)

    # Объединяем информацию о квартирах в одну строку
    all_info = "\n".join(flats_info)

    # Разделяем текст на части
    text_parts = split_text(all_info)

    for part in text_parts:
        await update.message.reply_text(part)
        
async def check_praga(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Информация по Таунхаусу в ЖК Прага: \n \n")

    praga_info = await parse_website(parse_praga)

    await update.message.reply_text(praga_info)


# Запуск бота
def main():
    # Создаем приложение
    application = Application.builder().token(TELEGRAM_TOKEN).read_timeout(30).build()

    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("zenit", check_zenit))
    application.add_handler(CommandHandler("sugar_valley", check_sugar_valley))
    application.add_handler(CommandHandler("praga", check_praga))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()