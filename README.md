##This is a mini server used to verify the validation of a word
##Usage

```
$ docker pull zlczlc/word_validation
$ docker run -p 5000:5000 zlczlc/word_validation
```

Usage 1:
Input "http://localhost:5000/login", input the test word in the form of the website and view the result.

Usage 2:
Open a python script and use the following command to test the validation.
```
import requests
testWord = "example"
response = requests.get("http://127.0.0.1:5000",params = {'word': testWord})
validation = bytes.decode(response.content)
```