import pytest
from ya_rest import YaApi


TEST_FOLDER = 'test_folder'


@pytest.fixture()
def create_folder():
    ya_client = YaApi()
    ya_client.create_folder(TEST_FOLDER)
    yield ya_client
    ya_client.delete_folder(TEST_FOLDER, True)
