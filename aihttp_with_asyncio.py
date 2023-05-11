import asyncio
import aiohttp


async def get_url_image(session):
    async with session.get('https://api.thecatapi.com/v1/images/search') as response:
        data = await response.json()
        return data[0]['url']


async def get_image_content(url_image, session):
    async with session.get(url_image) as image_manager:
        response_image = await image_manager.read()
        return response_image


async def main():
    async with aiohttp.ClientSession() as session:
        url_image = await get_url_image(session)
        name_and_extension_image = url_image.split('/')[-1]
        content_image = await get_image_content(url_image, session)
        await loop.run_in_executor(None, save_image, name_and_extension_image, content_image)


def save_image(name_and_extension_image, content_image):
    with open(f'Cats/{name_and_extension_image}', 'wb+') as writer:
        writer.write(content_image)
        print(f'Изображение {name_and_extension_image} записано!')


number_needed_images = 5
loop = asyncio.get_event_loop()
tasks = [loop.create_task(main()) for i in range(number_needed_images)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
