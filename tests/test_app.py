from io import BytesIO
import flask as Flask
from flask.testing import FlaskClient
import pytest

from src.app import app as my_app

FILE1 = "file1"
FILE2 = "file2"


@pytest.fixture()
def compare_files_app() -> Flask:
    app = my_app
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(compare_files_app: Flask) -> FlaskClient:
    return compare_files_app.test_client()


class TestApp:
    def test_status_code_root(self, client: FlaskClient):
        """
        Test if the root URL returns a status code of 200.
        """
        response = client.get("/")
        assert response.status_code == 200

    def test_same_files(self, client: FlaskClient, get_same_files: tuple[bytes, bytes]):
        """
        Test if the server correctly identifies identical files.
        """
        file1, file2 = get_same_files
        data = {FILE1: (BytesIO(file1), "puppy.jpg"), FILE2: (BytesIO(file2), "puppy_copy.jpg")}

        response = client.post(
            "/check-documents",
            data=data,
        )

        assert response.status_code == 200
        assert response.data == b"Files are the same!"

    def test_different_files(self, client: FlaskClient, get_different_files: tuple[bytes, bytes]):
        """
        Test if the server correctly identifies different files.
        """
        file1, file2 = get_different_files
        data = {FILE1: (BytesIO(file1), "text.txt"), FILE2: (BytesIO(file2), "text_different.txt")}

        response = client.post(
            "/check-documents",
            data=data,
        )

        assert response.status_code == 200
        assert response.data == b"Files are different!"
