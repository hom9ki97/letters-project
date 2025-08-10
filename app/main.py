from faker import Faker
import asyncio
from base import UserLetter, get_db, create_tables

faker = Faker()


def create_fake_data() -> dict:
    username = faker.first_name()
    time_sleep = faker.random_int(1, 10)
    email = f'{username}{faker.first_name()}@{faker.domain_name()}'
    text = faker.text()

    data = {
        'username': username,
        'time_sleep': time_sleep,
        'email': email,
        'text': text
    }
    return data


async def save_data_to_db(data: dict):
    async with get_db() as session:
        session.add(UserLetter(
            username=data['username'],
            email=data['email'],
            text=data['text'],
            delay=data['time_sleep']
        ))
        await session.commit()


async def create_fake_data_async():
    loop = asyncio.get_running_loop()

    return await loop.run_in_executor(None, create_fake_data)


async def push_email(data: dict):
    print(f"→ Начало отправки для {data['username']} (займёт {data['time_sleep']} сек)")
    await save_data_to_db(data)
    await asyncio.sleep(data['time_sleep'])
    print(f"✓ Email для {data['username']} отправлен!")


async def main():
    await create_tables()
    while True:
        tasks = [asyncio.create_task(process_single_data()) for _ in range(10)]
        await asyncio.gather(*tasks)
        print('✓ Все данные отправлены!\n')
        await asyncio.sleep(5)


async def process_single_data():
    data = await create_fake_data_async()
    await push_email(data)


if __name__ == '__main__':
    asyncio.run(main())
