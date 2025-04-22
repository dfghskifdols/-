import time
import asyncio
from hikka import hikka, events

# Старт юзербота
@hikka.on(events.NewMessage)
async def handler(event):
    # Чекаємо на повідомлення "/get_reward"
    if event.text == "/get_reward":
        # Перевірка кількості квитків з бази даних
        # Замініть цей код на логіку перевірки кількості квитків у вашій базі
        tickets = 15  # Приклад, тут має бути код для отримання реальної кількості квитків

        if tickets >= 15:
            # Якщо квитків більше або дорівнює 15, надсилаємо команду "дать миф 1"
            await event.respond("дать миф 1")
            # Затримка на 3 секунди, щоб дати час на виконання команди
            await asyncio.sleep(3)
            # Видаляємо своє повідомлення
            await event.delete()

# Запуск юзербота
hikka.run()
