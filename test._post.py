import requests
from tests.paths import PUPPY_COPY_PATH, PUPPY_PATH

# before running this, make sure that the flask app is running


files = {
    "file1": open(PUPPY_PATH, "rb"),
    "file2": open(PUPPY_COPY_PATH, "rb"),
}

result = requests.post("http://localhost:5011/check-documents", files=files)

print(result.content)
