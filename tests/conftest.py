import pytest

from .paths import PUPPY_COPY_PATH, PUPPY_PATH, TEXT_PATH, TEXT_DIFFERENT_PATH


@pytest.fixture()
def get_same_files():
    with open(PUPPY_PATH, "rb") as f1, open(PUPPY_COPY_PATH, "rb") as f2:
        file1 = f1.read()
        file2 = f2.read()
    return file1, file2


@pytest.fixture()
def get_different_files():
    with open(TEXT_PATH, "rb") as f1, open(TEXT_DIFFERENT_PATH, "rb") as f2:
        file1 = f1.read()
        file2 = f2.read()
    return file1, file2
