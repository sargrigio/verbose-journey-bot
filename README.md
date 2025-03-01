# Historical Saratov Bot

Этот бот для Telegram автоматически ищет информацию и изображения о событиях в Саратове, произошедших 120 лет назад относительно текущей даты.

## 🚀 Функционал
- Определяет дату 120 лет назад
- Ищет историческую информацию в интернете
- Ищет старые фотографии, открытки и иллюстрации
- Отправляет пользователю текст и изображения

## 📌 Установка и запуск локально

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/historical-saratov-bot.git
   cd historical-saratov-bot
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate  # Для Windows
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
4. Создайте файл `.env` и добавьте в него токен бота:
   ```
   BOT_TOKEN=your_telegram_bot_token
   ```
5. Запустите бота:
   ```sh
   python main.py
   ```

## 🌐 Развертывание на Render

1. Создайте репозиторий на GitHub и загрузите туда файлы.
2. Перейдите на [Render](https://dashboard.render.com/) и создайте **New Web Service**.
3. Подключите свой репозиторий и настройте сервис:
   - **Environment:** Python 3.x
   - **Start Command:** `python main.py`
4. В разделе **Environment Variables** добавьте `BOT_TOKEN`.
5. Нажмите **Deploy**.

После развертывания бот будет работать 24/7. 🎉

## 🛠 Требования
- Python 3.7+
- Библиотеки из `requirements.txt` (aiogram, logging, datetime)

## 📞 Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной через Telegram или создайте issue на GitHub!

