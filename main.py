import logging
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from web import search  # Инструмент для поиска информации в интернете

# Твой токен от BotFather
TOKEN = "YOUR_BOT_TOKEN"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функция вычисления даты 120 лет назад
def get_historical_date():
    today = datetime.date.today()
    historical_date = today.replace(year=today.year - 120)
    return historical_date.strftime("%d %B %Y")

# Функция поиска информации в интернете
def search_historical_info(date):
    query = f"Саратов {date} события 1905 года"
    results = search(query)
    return results if results else "Не удалось найти информацию. Попробуйте позже."

# Функция поиска исторических изображений
def search_historical_images(date):
    query = f"Старый Саратов {date} фото открытки 1905 год"
    image_results = search(query)
    return image_results if image_results else "Не удалось найти изображения. Попробуйте позже."

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Привет! Я помогу тебе узнать, что происходило в Саратове 120 лет назад. Введи /history, чтобы получить информацию.")

# Обработчик команды /history
@dp.message_handler(commands=["history"])
async def send_history(message: Message):
    date_120_years_ago = get_historical_date()
    response = f"Дата 120 лет назад: {date_120_years_ago}\n\nСейчас я найду информацию об этом дне..."
    await message.reply(response)
    
    # Поиск информации в интернете
    info = search_historical_info(date_120_years_ago)
    await message.reply(info)
    
    # Поиск изображений
    images = search_historical_images(date_120_years_ago)
    await message.reply(images)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
