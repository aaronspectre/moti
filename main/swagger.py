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
	def users(token):
		params = {
			'offset': '0',
			'paged': 'true',
			'pageNumber': '0',
			'pageSize': '100',
			'sort.sorted': 'true',
			'sort.unsorted': 'false',
			'unpaged': 'false'
		}
		response = json.loads(requests.get(ENDPOINT+'user', params = params, headers = {'Authorization': token}).text)
		return response['body']['content']


	@staticmethod
	def updateOrder(token, status, order_id):
		response = requests.put(f'{ENDPOINT}order/{order_id}', json = {'status': status}, headers = {'Authorization': token})


	@staticmethod
	def filter(status, token):
		params = {
			"direction": "ASC",
			"method": "APELSIN",
			"orderType": "DELIVERY",
			"page": 0,
			"size": 100,
			"sortBy": ["createdAt"]
		}
		response = json.loads(requests.post(ENDPOINT+'order/all', json = params, headers = {'Authorization': token}).text)
		return response


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
		response = json.loads(requests.get(ENDPOINT+'product/admin', params = params, headers = {'Authorization': token}).text)
		return response['content']


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
	def createProduct(token, request, product_id = None, update = False):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
		image = request.FILES['image']
		image.open(mode = 'rb')
		data = '{\n  "categoryId": '+request.POST['category']+',\n  "name": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['name_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['name_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['name_en']+'"\n    }\n  },\n  "discount": '+str(request.POST['discount'])+',\n  "description": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['desc_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['desc_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['desc_en']+'"\n    }\n  },\n  "price": '+str(request.POST['price'])+',\n  "readyTime": "'+str(request.POST['time'])+' min"\n}'
		data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T\r\nContent-Disposition: form-data; name=image; filename=Boys Cartoon Image.jpg\r\nContent-Type: image/jpeg\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
		if update:
			response = requests.put(f'{ENDPOINT}product/{product_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
		else:
			response = requests.post(ENDPOINT+'product', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
		image.close()


	@staticmethod
	def createCategory(token, raw, category_id = None, update = False):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
		data = '{\n    "categoryName": {\n      "uz": {\n        "lang": "uz",\n        "text": '+f'"{raw[0]}"'+'\n},\n      "ru": {\n        "lang": "ru",\n        "text": '+f'"{raw[1]}"'+'\n      },\n      "eng": {\n        "lang": "eng",\n        "text": '+f'"{raw[2]}"'+'\n      }\n    }\n  }'
		data = f"""--{boundary}\r\nContent-Disposition: form-data; name=categoryCreateRequest;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}--\r\n"""
		if update:
			response = requests.put(f'{ENDPOINT}category/{category_id}', data = data.encode(), headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
		else:
			response = requests.post(ENDPOINT+'category', data = data.encode(), headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})


	@staticmethod
	def deleteProduct(token, product_id):
		response = requests.delete(ENDPOINT+'product/'+str(product_id), headers = {'Authorization': token})


	@staticmethod
	def deleteCategory(token, product_id):
		response = requests.delete(ENDPOINT+'category/'+str(product_id), headers = {'Authorization': token})




if __name__ == '__main__':
	print('Swagger')