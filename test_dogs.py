import pytest
from allure import title
from conftest import TEST_FOLDER
from helper import upload_photos, get_random_breeds


class TestDogs:

    @title('Загрузка картинок собак')
    @pytest.mark.parametrize('breed', get_random_breeds(), ids=['without_subs', 'with_subs'])
    def test_upload_dog(self, breed, create_folder):
        sub_breeds, response = upload_photos(breed, TEST_FOLDER)
        assert response['type'] == 'dir', 'Тип файла отличается от dir'
        assert response['name'] == TEST_FOLDER, f'Имя папки отличается отличается от {TEST_FOLDER}'
        items = response['_embedded']['items']
        if sub_breeds:
            assert len(items) == len(sub_breeds), f'Количество файлов внутри папки отличается от {len(sub_breeds)}'
        else:
            assert len(items) == 1, 'Количество файлов внутри папки отличается от 1'
        for item in items:
            assert item['type'] == 'file', 'Тип файла отличается от file'
            assert item['name'].startswith(breed), f'Имя файла не начинается с {breed}'
