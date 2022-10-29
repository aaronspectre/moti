import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("{{host1}}ranch")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=request;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("""{
    \"addressId\": 1,
    \"capacity\": 12128,
    \"contacts\": \"8987edit 783116728\",
    \"deletedImages\": [
      \"https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/23e0d1ea-d9d3-4736-97e5-23d8c895d205Screen+Shot+2022-09-16+at+12.39.36.png?alt=media\",
      \"https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/f736f58d-8f19-40d1-a3c8-7a22691d8d39Screen+Shot+2022-09-16+at+12.39.39.png?alt=media\",
      \"https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/ffca292b-3032-4728-9c32-7384d01a13a6Screen+Shot+2022-09-16+at+12.39.41.png?alt=media\"
    ],
    \"information\": {
      \"uz\": {
        \"lang\": \"uz\",
        \"text\": \"oybek edit  m11111euhca\"
      },
      \"ru\": {
        \"lang\": \"ru\",
        \"text\": \"11111  edit sub\"
      },
      \"eng\": {
        \"lang\": \"eng\",
        \"text\": \"ingli111zcecweec edit   sub\"
      }
    },
    \"target\": \"oybek111 edit  metro \"
  }"""))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
print(body)
# payload = body
# headers = {
#    'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
# }
# conn.request("PUT", "/admin/1", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))