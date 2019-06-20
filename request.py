from urllib.parse import urlencode
from urllib.request import urlopen, Request

httpresponse = urlopen('http://example.com')
body = httpresponse.read()
print(body)


# post
data = {
    'email': 'dickscar@gmail.com',
    'password': '1234',
    'name': '윤민호'
}
data = urlencode(data).encode('utf-8')
print(data)

request = Request('http://www.example.com', data)
httpresponse = urlopen(request)
print(httpresponse.read())
