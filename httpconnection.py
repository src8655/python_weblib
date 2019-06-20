from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET /HTTP/1.1
# 200 OK
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason, type(resp.status))

if resp.status == 200:
    body = resp.read()
    print(body)


# 성공
# GET /hello.html HTTP/1.1
# 404 File Not Found
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason, type(resp.status))

if resp.status == 404:
    body = resp.read()
    print(body)
