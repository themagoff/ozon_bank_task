import os
from dotenv import load_dotenv, find_dotenv
import requests
from requests.models import Response


class YaApi:

    load_dotenv(find_dotenv())
    token = os.getenv('TOKEN')
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, path: str) -> Response:
        return requests.put(f'{self.url}?path={path}', headers=self.headers)

    def get_folder(self, path: str) -> Response:
        return requests.get(f'{self.url}?path={path}', headers=self.headers)

    def delete_folder(self, path: str, permanently: bool) -> Response:
        params = {'path': path, 'permanently': permanently}
        return requests.delete(f'{self.url}?path={path}', headers=self.headers, params=params)

    def upload_photos_to_yd(self, path: str, url_file: str, name: str) -> Response:
        params = {'path': f'/{path}/{name}', 'url': url_file, 'overwrite': 'true'}
        return requests.post(f'{self.url}/upload', headers=self.headers, params=params)
