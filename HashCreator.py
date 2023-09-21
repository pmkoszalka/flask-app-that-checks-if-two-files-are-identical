import argparse
import hashlib


def add_arguments() -> argparse.Namespace:
    """
    Parse command line arguments for calculating SHA-256 hash of two files.
    """
    parser = argparse.ArgumentParser(description="Calculate SHA-256 hash of a file.")
    parser.add_argument("first_file_path", type=str, help="Path to the first file file")
    parser.add_argument("second_file_path", type=str, help="Path to the second file file")
    args = parser.parse_args()
    return args


class HashCreator:
    """
    A class for creating and comparing SHA-256 hashes of files.
    """

    def __init__(self):
        pass

    def calculate_sha256_hash(self, file: bytes) -> str:
        """
        Calculate the SHA-256 hash of a file.
        """
        sha256_hash = hashlib.sha256()
        sha256_hash.update(file)
        return sha256_hash.hexdigest()

    def check_if_files_the_same(self, first_file: bytes, second_file: bytes) -> str:
        """
        Compare SHA-256 hashes of two files to check if they are the same.
        """
        if self.calculate_sha256_hash(first_file) == self.calculate_sha256_hash(second_file):
            print("Files are the same!")
            return "Files are the same!"
        else:
            print("Files are not the same!")
            return "Files are different!"


if __name__ == "__main__":
    args = add_arguments()
    first_file_path = args.first_file_path
    second_file_path = args.second_file_path
    HashCreator().check_if_files_the_same(first_file=first_file_path, second_file=second_file_path)
