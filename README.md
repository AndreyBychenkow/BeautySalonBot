# 🖥️ Сервис BeautyCity

Telegram-бот для записи на процедуры в салонах красоты. Пользователи могут выбирать салон, мастера, процедуру, дату и время записи.

## ⚙️ Функциональность

- Запись через салон
- Запись через мастера
- Просмотр цен на процедуры
- Возможность позвонить администратору
- Интерактивное меню для удобства использования

### 📋 Предварительные требования

- Python 3.6 или выше
- Установленная библиотека `python-telegram-bot`
- Django 

## 🛠 Установка

1. 📌 **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Eugene571/beauty_city_bot.git
   ```

2. 📌 **Установите зависимости:**
   ```bash
   pip install -r requirements.txt   
   ```
## 🚀 Запуск

1. 📌 **Создайте файл .env в корне проекта и добавьте ваш токен бота::**
   ```bash
   TOKEN='ваш_токен_бота'   
   ```
   
2. 📌 **Запустите бота с помощью следующей команды:**
   ```bash
   python run_bot.py  
   ```

### 🔑 Использование


- Найдите вашего бота в Telegram (по имени, которое вы ему дали).

- Начните взаимодействие с ботом, нажав на кнопку "Старт".

- Следуйте инструкциям для записи на процедуры.

### 📺 Пример работы бота:

![Результат](https://i.postimg.cc/zG7ZKWRZ/25-12-2024-211659.gif)

🌟**Бот исключает возможность записи на одно и то же время !!!**🌟

3. 📌 **Проверьте результат:**

Используйте админку Django и войдите с учетными данными суперпользователя для управления cервиса BeautyCity.
   
![Результат](https://i.postimg.cc/KzL0rSsk/admin.jpg) 
   
   
## ✅ Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).