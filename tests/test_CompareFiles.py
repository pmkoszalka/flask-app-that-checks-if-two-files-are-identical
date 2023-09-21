import pytest
from pathlib import Path

from ..CompareFiles import CompareFiles

TESTCASES_PATH = Path.cwd() / "tests" / "testcases"

PUPPY_PATH = TESTCASES_PATH / "puppy.jpg"
PUPPY_COPY_PATH = TESTCASES_PATH / "puppy_copy.jpg"
TEXT_PATH = TESTCASES_PATH / "text.txt"
TEXT_DIFFERENT_PATH = TESTCASES_PATH / "text_different.txt"


@pytest.fixture
def compare_files() -> CompareFiles:
    return CompareFiles()


class TestCompareFiles:
    def test_same_files(self, compare_files: CompareFiles):
        with open(PUPPY_PATH, "rb") as f1, open(PUPPY_COPY_PATH, "rb") as f2:
            file1 = f1.read()
            file2 = f2.read()
        assert compare_files.check_if_files_the_same(file1, file2) is True

    def test_different_files(self, compare_files: CompareFiles):
        with open(TEXT_PATH, "rb") as f1, open(TEXT_DIFFERENT_PATH, "rb") as f2:
            file1 = f1.read()
            file2 = f2.read()
        assert compare_files.check_if_files_the_same(file1, file2) is False
