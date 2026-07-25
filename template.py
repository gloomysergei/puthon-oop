from urllib.parse import urlparse

url = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
print(url.geturl())