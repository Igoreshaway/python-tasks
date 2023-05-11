import requests
import asyncio


async def get_url_image():
    search_random_image_url = 'https://api.thecatapi.com/v1/images/search'
    response = await loop.run_in_executor(None, requests.get, search_random_image_url)
    return response.json()[0]['url']


async def get_image_content(url):
    response_image = await loop.run_in_executor(None, requests.get, url)
    print(f'Изображение {url.split("/")[-1]} получено, но не записано.')
    return response_image.content


async def get_and_save_cat_image():
    image_url = await get_url_image()
    image_name_and_extension = image_url.split('/')[-1]
    image_content = await get_image_content(image_url)

    await loop.run_in_executor(None, save_image, image_name_and_extension, image_content)


def save_image(image_name_and_extension, image_content):
    with open(f'Cats/{image_name_and_extension}', 'wb+') as writer:
        writer.write(image_content)
        print(f'Изображение {image_name_and_extension} записано!')


number_needed_images = 5
loop = asyncio.get_event_loop()
tasks = [loop.create_task(get_and_save_cat_image()) for i in range(number_needed_images)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
