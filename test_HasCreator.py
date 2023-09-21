import unittest
from app import app

class TestHashCreator(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_same_files(self):
        with open('test_file.txt', 'rb') as f:
            file1 = f.read()
            file2 = f.read()
        response = self.client.post('/', data={
            'file1': file1,
            'file2': file2
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'True')

    def test_different_files(self):
        with open('test_file1.txt', 'rb') as f1, open('test_file2.txt', 'rb') as f2:
            file1 = f1.read()
            file2 = f2.read()
        response = self.client.post('/', data={
            'file1': file1,
            'file2': file2
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'False')

if __name__ == '__main__':
    unittest.main()