**cuurency-bot** — это учебный проект, представляющий собой пример Telegram-бота для для конвертации валют.

## Описание

Данный бот позволяет конвертировать вылюту. Проект создан в качестве учебного на Skillfactory.

## Технологии

В проекте используются следующие технологии:

- **pyTelegramBotAPI** 4.26.0 — фреймворк для разработки Telegram-ботов.
- **pydantic-settings** 2.7.0 — управление настройками с использованием Pydantic.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ReutAS39/currency-bot.git
   ```

2. Перейдите в директорию проекта:

   ```bash
   cd currency-bot
   ```

3. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

4. Получите токен бота через [@BotFather](https://t.me/BotFather).

5. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

6. Создайте файл `.env` в корне проекта:

   ```
   BOT_TOKEN=ВАШ_ТОКЕН
   ```

