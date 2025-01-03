from faker import Faker

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_bot.settings')
django.setup()

from bot.models import Salon, Specialist

fake = Faker('ru_RU')


for _ in range(3):
    Salon.objects.create(
        name=fake.company(),
        address=fake.address(),
        phone=fake.phone_number(),
        email=fake.email(),
        opening_time="09:00:00",
        closing_time="20:00:00"
    )

for _ in range(5):
    Specialist.objects.create(
        name=fake.first_name(),
        phone=fake.phone_number()
    )


print("Случайные данные сгенерированы.")
