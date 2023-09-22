# overview
This project is a simple flask app that allows you to check if two files are identical or different. Additionally, it includes tests. 

## Examplary curl:
```
$ curl -X POST -F file1=@tests/testcases/puppy.jpg -F file2=@tests/testcases/puppy_copy.jpg http://localhost:5011/check-documents
```

## To run test, run the command:
```
$ cd <path-to-project>
$ pytest
```