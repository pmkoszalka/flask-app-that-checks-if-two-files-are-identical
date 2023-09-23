import requests
from pathlib import Path

# before running this, make sure that the flask app is running

path_to_testcases = Path.cwd() / "tests" / "testcases"

files = {
    "file1": open(path_to_testcases / "puppy.jpg", "rb"),
    "file2": open(path_to_testcases / "puppy_copy.jpg", "rb"),
}

result = requests.post("http://localhost:5011/check-documents", files=files)

print(result.content)
