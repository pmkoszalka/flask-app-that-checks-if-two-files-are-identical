import pytest

from src.CompareFiles import CompareFiles


@pytest.fixture
def compare_files() -> CompareFiles:
    return CompareFiles()


class TestCompareFiles:
    def test_same_files(self, compare_files: CompareFiles, get_same_files: tuple[bytes, bytes]):
        """
        Test if two identical files are recognized as the same.
        """
        file1, file2 = get_same_files
        assert compare_files.check_if_files_the_same(file1, file2) is True

    def test_different_files(
        self, compare_files: CompareFiles, get_different_files: tuple[bytes, bytes]
    ):
        """
        Test if two different files are recognized as different.
        """
        file1, file2 = get_different_files
        assert compare_files.check_if_files_the_same(file1, file2) is False
