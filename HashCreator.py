import hashlib
import argparse

class HashCreator:
    def __init__(self):
        pass

    def calculate_sha256_hash(self, document):
        sha256_hash = hashlib.sha256()

        with open(document, 'rb') as file:
            while chunk := file.read(4096):  # Read the document in 4KB chunks
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    def calculate_md5_hash(self,  document_path):
        md5_hash = hashlib.md5()

        with open(document_path, 'rb') as file:
            while chunk := file.read(4096):  # Read the document in 4KB chunks
                md5_hash.update(chunk)

        print(md5_hash.hexdigest())
        return md5_hash.hexdigest()

    def check_if_files_the_same(self, first_document: str, second_document: str):
        if self.calculate_sha256_hash(first_document) == self.calculate_sha256_hash(second_document):
            print("Documents are the same!")
        else:
            print("Documents are different!")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate SHA-256 hash of a document.')
    parser.add_argument('document_path', type=str, help='Path to the first document file')
    parser.add_argument('document_path2', type=str, help='Path to the second document file')
    args = parser.parse_args()
    first_document_path = args.document_path
    second_document_path = args.document_path2
    HashCreator().check_if_files_the_same(first_document=first_document_path, second_document=second_document_path)
