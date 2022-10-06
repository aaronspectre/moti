import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("drogrammer.uz", None)
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=request;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("""{
  \"categoryId\": 7,
  \"name\": {
    \"uz\": {
      \"lang\": \"uz\",
      \"text\": \"Losos balig'lik Maki\"
    },
    \"ru\": {
      \"lang\": \"ru\",
      \"text\": \"Маки с лососем \"
    },
    \"eng\": {
      \"lang\": \"eng\",
      \"text\": \"Maki with salmon\"
    }
  },
  \"discount\": 0.1,
  \"description\": {
    \"uz\": {
      \"lang\": \"uz\",
      \"text\": \"Salmon Maki Rolls sushining eng taniqli shaklidir. Ular xom yangi losos va piyoz bilan to'ldirilgan va nori (dengiz o'tlari) bilan o'ralgan sushi guruchining klassik rulonlari\"
    },
    \"ru\": {
      \"lang\": \"ru\",
      \"text\": \"Роллы с лососем маки — самая узнаваемая форма суши. Это классические роллы из риса для суши, фаршированные сырым свежим лососем и зеленым луком и завернутые в нори (морские водоросли).\"
    },
    \"eng\": {
      \"lang\": \"eng\",
      \"text\": \"Salmon Maki Rolls are the most recognisable form of Sushi. They're the classic rolls of sushi rice stuffed with raw fresh salmon and spring onion and wrapped in nori (seaweed). \"
    }
  },
  \"price\": 39000,
  \"readyTime\": \"45 min\"
}"""))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format('Boys Cartoon Image.jpg')))

fileType = mimetypes.guess_type('C:/Users/localhost/Downloads/pic.jpg')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('C:/Users/localhost/Downloads/pic.jpg', 'rb') as f:
  dataList.append(f.read())
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
   'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5OTg5NzYzMzE4MDkiLCJyb2xlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJST0xFX0FETUlOIn1dLCJpYXQiOjE2NjQwOTc2NTcsImV4cCI6Mzc2NjQwOTc2NTd9.ORHHPOHwcEerLfi4_DGhPvZOwWTyNDvcXuxjR01OLyrlOl_lJldx97VY5UjZ1ntiR9A4Hi8r9J8PBvEKtpkUgg',
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
}
# conn.request("POST", "/api/v1/product", payload, headers)
# res = conn.getresponse()
# data = res.read()
print(payload)
print(data.decode("utf-8"))