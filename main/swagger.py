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
	def update_user(token, data, user_id):
		data = {
			'name': data['first_name'],
			'roles': data['user-roles'].split(' | ')
		}
		response = requests.put(f'{ENDPOINT}user/admin/{user_id}', json = data, headers = {'Authorization': token})


	@staticmethod
	def create_order(token, data):
		data = {
			"addressId": int(data['address']),
			"branchId": int(data['branch']),
			"comment": data['comment'],
			"deliveryTime": data['delivery'],
			"distance": int(data['distance']),
			"orderType": data['order-type'],
			"paymeType": data['payment'],
			"products": json.loads(data['orders'])
		}
		response = requests.post(f'{ENDPOINT}order', json = data, headers = {'Authorization': token})


	@staticmethod
	def updateOrder(token, status, order_id):
		response = requests.put(f'{ENDPOINT}order/{order_id}', json = {'status': status}, headers = {'Authorization': token})


	@staticmethod
	def filter(token, order_type, payment):
		params = {
			"direction": "ASC",
			"method": payment,
			"orderType": order_type,
			"page": 0,
			"size": 100,
			"sortBy": ["createdAt"]
		}
		response = json.loads(requests.post(ENDPOINT+'order/all', json = params, headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def branches(token):
		return json.loads(requests.get(f'{ENDPOINT}branch', headers = {'Authorization': token}).text)


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
		if update:
			data = '{\n  "categoryId": '+request.POST['category']+',\n  "name": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['name_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['name_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['name_en']+'"\n    }\n  },\n  "discount": '+str(request.POST['discount'])+',\n  "description": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['desc_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['desc_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['desc_en']+'"\n    }\n  },\n  "price": '+str(request.POST['price'])+',\n  "readyTime": "'+str(request.POST['time'])+' min"\n}'
			if 'image' in request.FILES:
				image = request.FILES['image']
				image.open(mode = 'rb')
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename=Boys Cartoon Image.jpg\r\nContent-Type: image/jpeg\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}product/{product_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
				image.close()
			else:
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}'.encode(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}product/{product_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
		else:
			image = request.FILES['image']
			image.open(mode = 'rb')
			data = '{\n  "categoryId": '+request.POST['category']+',\n  "name": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['name_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['name_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['name_en']+'"\n    }\n  },\n  "discount": '+str(request.POST['discount'])+',\n  "description": {\n    "uz": {\n      "lang": "uz",\n      "text": "'+request.POST['desc_uz']+'"\n    },\n    "ru": {\n      "lang": "ru",\n      "text": "'+request.POST['desc_ru']+'"\n    },\n    "eng": {\n      "lang": "eng",\n      "text": "'+request.POST['desc_en']+'"\n    }\n  },\n  "price": '+str(request.POST['price'])+',\n  "readyTime": "'+str(request.POST['time'])+' min"\n}'
			data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename=Boys Cartoon Image.jpg\r\nContent-Type: image/jpeg\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
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


	@staticmethod
	def fees(token):
		response = json.loads(requests.get(ENDPOINT+'fee', headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def add_fee(token, data):
		data = {
			'deliveryPayment': float(data['payment']),
			'price': float(data['price'])
		}
		response = requests.post(ENDPOINT+'fee', json = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})
		return response


	@staticmethod
	def update_fee(token, fee_id, data):
		data = {
			'deliveryPayment': float(data['payment']),
			'price': float(data['price'])
		}
		response = requests.put(f'{ENDPOINT}fee/{fee_id}', json = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})



if __name__ == '__main__':
	print('Swagger')