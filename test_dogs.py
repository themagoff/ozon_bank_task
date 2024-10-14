import pytest
from allure import title
from helper import upload_photos, delete_photos, get_random_breeds


class TestDogs:

    @title('Загрузка картинок собак')
    @pytest.mark.parametrize('breed', get_random_breeds())
    def test_upload_dog(self, breed):
        folder = 'test_folder'
        try:
            sub_breeds, response = upload_photos(breed, folder)
            assert response['type'] == 'dir', 'Тип файла отличается от dir'
            assert response['name'] == folder, f'Имя папки отличается отличается от {folder}'
            items = response['_embedded']['items']
            if sub_breeds:
                assert len(items) == len(sub_breeds), f'Количество файлов внутри папки отличается от {len(sub_breeds)}'
            else:
                assert len(items) == 1, 'Количество файлов внутри папки отличается от 1'
            for item in items:
                assert item['type'] == 'file', 'Тип файла отличается от file'
                assert item['name'].startswith(breed), f'Имя файла не начинается с {breed}'
        finally:
            delete_photos(folder)
