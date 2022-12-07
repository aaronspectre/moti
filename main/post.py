import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("admin.motitashkent.uz")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=product;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("""{
  \"available\": true,
  \"categoryId\": 2,
  \"code\": \"string\",
  \"description\": {
    \"en\": \"string\",
    \"ru\": \"string\",
    \"uz\": \"string\"
  },
  \"discount\": 0,
  \"name\": {
    \"en\": \"string\",
    \"ru\": \"string\",
    \"uz\": \"string\"
  },
  \"price\": 1200,
  \"readyTime\": 10
}"""))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format('image.png')))

fileType = mimetypes.guess_type('/home/fedora/Downloads/image.png')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/home/fedora/Downloads/image.png', 'rb') as f:
  dataList.append(b'image')
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary),
   'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5OTg5NzYzMzE4MDkiLCJyb2xlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9BRE1JTiJ9XSwiaWF0IjoxNjcwNDA3NzkwLCJleHAiOjE2NzA0OTQxOTB9.rJFkC22764wTiRfgQZNNlE3jH496NPKFLE7egHXQ0bq7PfvidvybikYZZtwLim3BuxKgHSQelB-YwhKdKArbXg'
}
print(payload.decode())
# conn.request("POST", "/api/v1/product/admin", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))