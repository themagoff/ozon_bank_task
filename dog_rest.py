import requests
from requests import Response


class DogApi:

    url = 'https://dog.ceo/api/breed'

    def get_breed_list(self, breed: str) -> Response:
        return requests.get(f'{self.url}/{breed}/list')

    def get_random_breed_image(self, breed: str) -> Response:
        return requests.get(f'{self.url}/{breed}/images/random')

    def get_random_sub_breed_image(self, breed: str, sub_breed: str) -> Response:
        return requests.get(f'{self.url}/{breed}/{sub_breed}/images/random')

    def get_all_breeds(self) -> Response:
        return requests.get(f'{self.url}s/list/all')
