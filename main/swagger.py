import json
import requests


ENDPOINT = 'http://drogrammer.uz/api/v1/'

class Swagger:
	@staticmethod
	def auth(username, password):
		data = {'phonenumber': username, 'password': password}
		response = json.loads(requests.post(ENDPOINT+'auth/login_admin', json = data).text)
		return response


	@staticmethod
	def filter(status, token):
		params = {
			'from': '0',
			'paged': 'false',
			'sort.sorted': 'true',
			'sort.unsorted': 'false',
			'status': status,
			'to': '100',
			'unpaged': 'true'
		}
		response = json.loads(requests.get(ENDPOINT+'order', params = params, headers = {'Authorization': token}).text)
		return response['data'] if not response == list() else []


	@staticmethod
	def products(token):
		params = {
			'offset': '0',
			'paged': 'true',
			'pageNumber': '0',
			'pageSize': '100',
			'sort.sorted': 'true',
			'sort.unsorted': 'false',
			'unpaged': 'false',
		}
		response = json.loads(requests.get(ENDPOINT+'product', params = params, headers = {'Authorization': token}).text)


	@staticmethod
	def categories(token):
		params = {
			'offset': '0',
			'paged': 'true',
			'pageNumber': '0',
			'pageSize': '100',
			'sort.sorted': 'true',
			'sort.unsorted': 'false',
			'unpaged': 'false',
		}
		response = json.loads(requests.get(ENDPOINT+'category/page', params = params, headers = {'Authorization': token}).text)
		return response['content']


	@staticmethod
	def createProduct(token, raw):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'


	@staticmethod
	def createCategory(token, raw):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
		data = '{\n    "categoryName": {\n      "uz": {\n        "lang": "uz",\n        "text": '+f'"{raw[0]}"'+'\n},\n      "ru": {\n        "lang": "ru",\n        "text": '+f'"{raw[1]}"'+'\n      },\n      "eng": {\n        "lang": "eng",\n        "text": '+f'"{raw[2]}"'+'\n      }\n    }\n  }'
		data = f"""--{boundary}\r\nContent-Disposition: form-data; name=categoryCreateRequest;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}--\r\n"""
		print(data)
		response = requests.post(ENDPOINT+'category', data = data.encode(), headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})