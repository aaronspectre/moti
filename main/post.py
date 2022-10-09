import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("drogrammer.uz", None)
dataList = []


def get_post():
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
         \"text\": \"Name\"
       },
       \"ru\": {
         \"lang\": \"ru\",
         \"text\": \"Name\"
       },
       \"eng\": {
         \"lang\": \"eng\",
         \"text\": \"Name\"
       }
     },
     \"discount\": 0,
     \"description\": {
       \"uz\": {
         \"lang\": \"uz\",
         \"text\": \"Name\"
       },
       \"ru\": {
         \"lang\": \"ru\",
         \"text\": \"Name\"
       },
       \"eng\": {
         \"lang\": \"eng\",
         \"text\": \"Name\"
       }
     },
     \"price\": 0,
     \"readyTime\": \"0 min\"
   }"""))
   dataList.append(encode('--' + boundary))
   dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format('Boys Cartoon Image.jpg')))

   fileType = mimetypes.guess_type('C:/Users/localhost/Downloads/pic.jpg')[0] or 'application/octet-stream'
   dataList.append(encode('Content-Type: {}'.format(fileType)))
   dataList.append(encode(''))

   with open('C:/Users/localhost/Downloads/pic.jpg', 'r') as f:
     dataList.append(f.read())
     # dataList.append(encode('IMAGE'))
   dataList.append(encode('--'+boundary+'--'))
   dataList.append(encode(''))
   body = b'\r\n'.join(dataList)
   payload = body
   headers = {
      'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5OTg5NzYzMzE4MDkiLCJyb2xlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJST0xFX0FETUlOIn1dLCJpYXQiOjE2NjQwOTc2NTcsImV4cCI6Mzc2NjQwOTc2NTd9.ORHHPOHwcEerLfi4_DGhPvZOwWTyNDvcXuxjR01OLyrlOl_lJldx97VY5UjZ1ntiR9A4Hi8r9J8PBvEKtpkUgg',
      'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
   }
   return payload
# conn.request("POST", "/api/v1/product", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))
request = """--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{\n  "categoryId": 7,\n  "name": {\n    "uz": {\n      "lang": "uz",\n      "text": "Losos balig\'lik Maki"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "\xd0\x9c\xd0\xb0\xd0\xba\xd0\xb8 \xd1\x81 \xd0\xbb\xd0\xbe\xd1\x81\xd0\xbe\xd1\x81\xd0\xb5\xd0\xbc "\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "Maki with salmon"\n    }\n  },\n  "discount": 0.1,\n  "description": {\n    "uz": {\n      "lang": "uz",\n      "text": "Salmon Maki Rolls sushining eng taniqli shaklidir. Ular xom yangi losos va piyoz bilan to\'ldirilgan va nori (dengiz o\'tlari) bilan o\'ralgan sushi guruchining klassik rulonlari"\n    },\n    "ru": {\n      "lang": "ru",\n      "text":"Some Text"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "Salmon Maki Rolls are the most recognisable form of Sushi. They\'re the classic rolls of sushi rice stuffed with raw fresh salmon and spring onion and wrapped in nori (seaweed). "\n    }\n  },\n  "price": 39000,\n  "readyTime": "45 min"\n}\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T\r\nContent-Disposition: form-data; name=image; filename=Boys Cartoon Image.jpg\r\nContent-Type: image/jpeg\r\n\r\nIMAGE\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n"""