import pytest

from File import File

NAME = "datos.txt"


@pytest.fixture
def file():
    return File(NAME)


def test_file_esentials(file):
    file.save_data("datos")
    assert file.exists() is True
    file.delete()
    assert file.exists() is False
    assert file.delete() is False


def test_save_and_load(file):
    data = "more data"
    file.save_data(data)
    assert file.extract_data() == data
    file.delete()
