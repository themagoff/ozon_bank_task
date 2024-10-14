from random import choice
import time
from ya_rest import YaApi
from dog_rest import DogApi


def get_sub_breeds(breed: str) -> list[str]:
    return dog_client.get_breed_list(breed).json().get('message', [])


def get_urls(breed: str, sub_breeds: list[str]) -> list[str]:
    url_images = []
    if sub_breeds:
        for sub_breed in sub_breeds:
            url_images.append(dog_client.get_random_sub_breed_image(breed, sub_breed).json().get('message'))
    else:
        url_images.append(dog_client.get_random_breed_image(breed).json().get('message'))
    return url_images


def upload_photos(breed: str, folder: str) -> tuple:
    sub_breeds = get_sub_breeds(breed)
    urls = get_urls(breed, sub_breeds)
    ya_client.create_folder(folder)
    for url in urls:
        part_name = url.split('/')
        name = '_'.join([part_name[-2], part_name[-1]])
        ya_client.upload_photos_to_yd(folder, url, name)
    time.sleep(3)
    return sub_breeds, ya_client.get_folder(folder).json()


def delete_photos(folder: str, permanently: bool = True) -> None:
    ya_client.delete_folder(folder, permanently)


def get_random_breeds() -> list[str]:
    all_breeds = dog_client.get_all_breeds().json().get('message')
    without_subs = []
    with_subs = []
    for k, v in all_breeds.items():
        if len(v) == 0:
            without_subs.append(k)
        else:
            with_subs.append(k)
    return [choice(without_subs), choice(with_subs)]


dog_client = DogApi()
ya_client = YaApi()
