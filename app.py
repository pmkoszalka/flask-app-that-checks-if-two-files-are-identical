from flask import Flask, request
from CompareFiles import CompareFiles

DEBUG = True
HOST = "0.0.0.0"
PORT = 5011

app = Flask(__name__)
hash_creator = CompareFiles()


@app.route("/", methods=["GET"])
def redirect_to_proper_route() -> str:
    """
    Redirects to the proper route for checking if documents are the same.
    """
    return "To check if documents are the same after port add '/check-documents'"


@app.route("/check-documents", methods=["POST"])
def check_if_documents_the_same() -> str:
    """
    Checks if two uploaded files are the same.
    """
    try:
        file1 = request.files["file1"].read()
        file2 = request.files["file2"].read()
        result = hash_creator.check_if_files_the_same(file1, file2)

        if not result:
            return "The documents are different!"
        return "The documents are same!"

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host=HOST, debug=DEBUG, port=PORT)
