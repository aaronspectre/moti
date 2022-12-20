import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("admin.motitashkent.uz")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=advert;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("""{
  \"title\": {
    \"en\": \"Discount\",
    \"ru\": \"string\",
    \"uz\": \"Chegirma\"
  },
  \"content\": {
    \"en\": \"increase\",
    \"ru\": \"nose\",
    \"uz\": \"cure\"
  }
}"""))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format('image.jpg')))

fileType = mimetypes.guess_type('/home/fedora/Downloads/Trash/image.jpg')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/home/fedora/Downloads/Trash/image.jpg', 'rb') as f:
  # dataList.append(f.read())
  dataList.append(b"image")
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
print(payload.decode())
# headers = {
#    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
# }
# conn.request("POST", "/api/v1/advert/admin", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))