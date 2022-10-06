import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("drogrammer.uz", None)
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=categoryCreateRequest;'))

dataList.append(encode('Content-Type: {}'.format('application/json')))
dataList.append(encode(''))

dataList.append(encode("""{
    \"categoryName\": {
      \"uz\": {
        \"lang\": \"uz\",
        \"text\": \"uzbek sub\"
      },
      \"ru\": {
        \"lang\": \"ru\",
        \"text\": \"ruscha sub\"
      },
      \"eng\": {
        \"lang\": \"eng\",
        \"text\": \"ingliz  sub\"
      }
    }
  }"""))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
print(payload)
headers = {
   'Content-type': 'multipart/form-data; boundary={}'.format(boundary) ,
   'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5OTg5NzYzMzE4MDkiLCJyb2xlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJST0xFX0FETUlOIn1dLCJpYXQiOjE2NjQwOTc2NTcsImV4cCI6Mzc2NjQwOTc2NTd9.ORHHPOHwcEerLfi4_DGhPvZOwWTyNDvcXuxjR01OLyrlOl_lJldx97VY5UjZ1ntiR9A4Hi8r9J8PBvEKtpkUgg'
}
# conn.request("POST", "/api/v1//category", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


import requests

boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
data = {
	"categoryName": {
		"uz": {
			"lang": "uz",
			"text": "uzbek sub"
		},
		"ru": {
			"lang": "ru",
			"text": "ruscha sub"
		},
		"eng": {
			"lang": "eng",
			"text": "ingliz  sub"
		}
	}
}
data = '{\n    "categoryName": {\n      "uz": {\n        "lang": "uz",\n        "text": "uzbek sub"\n},\n      "ru": {\n        "lang": "ru",\n        "text": "ruscha sub"\n      },\n      "eng": {\n        "lang": "eng",\n        "text": "ingliz  sub"\n      }\n    }\n  }'
data = f"""--{boundary}\r\nContent-Disposition: form-data; name=categoryCreateRequest;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}--\r\n""".encode()
headers = {
	'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI5OTg5NzYzMzE4MDkiLCJyb2xlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJST0xFX0FETUlOIn1dLCJpYXQiOjE2NjQwOTc2NTcsImV4cCI6Mzc2NjQwOTc2NTd9.ORHHPOHwcEerLfi4_DGhPvZOwWTyNDvcXuxjR01OLyrlOl_lJldx97VY5UjZ1ntiR9A4Hi8r9J8PBvEKtpkUgg',
	'Content-Type': f'multipart/form-data; boundary={boundary}'
}

print(data)

response = requests.post('http://drogrammer.uz/api/v1/category', data = data, headers = headers)
print(response.text)