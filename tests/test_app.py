from io import BytesIO
import flask as Flask
from flask.testing import FlaskClient
import pytest

from ..app import app as my_app


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


class Test_App:
    def test_status_code_root(self, client: FlaskClient):
        response = client.get("/")
        assert response.status_code == 200

    def test_same_files(self, client: FlaskClient, get_same_files: tuple[bytes, bytes]):
        data = {}
        file1, file2 = get_same_files
        data["file1"] = (BytesIO(file1), "puppy.jpg")
        data["file2"] = (BytesIO(file2), "puppy_copy.jpg")

        response = client.post(
            "/check-documents",
            data=data,
        )

        assert response.status_code == 200
        assert response.data == b"Files are same!"

    def test_different_files(self, client: FlaskClient, get_different_files: tuple[bytes, bytes]):
        data = {}
        file1, file2 = get_different_files
        data["file1"] = (BytesIO(file1), "text.txt")
        data["file2"] = (BytesIO(file2), "text_different.txt")

        response = client.post(
            "/check-documents",
            data=data,
        )

        assert response.status_code == 200
        assert response.data == b"Files are different!"
