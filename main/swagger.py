import json
import requests


ENDPOINT = 'http://admin.motitashkent.uz/api/v1/'

class Swagger:
	@staticmethod
	def auth(username, password):
		data = '{\n    \"phone\": \"'+username+'\",\n    \"password\": \"'+password+'\"\n}'
		response = json.loads(requests.post(ENDPOINT+'auth/login', data = data, headers = {'Content-Type': 'application/json'}).text)
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
		response = json.loads(requests.get(ENDPOINT+'order', params = params, headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def branches(token):
		params = {
			'offset': '0',
			'paged': 'true',
			'pageNumber': '0',
			'pageSize': '100',
			'sort.sorted': 'true',
			'sort.unsorted': 'false',
			'unpaged': 'false',
		}
		return json.loads(requests.get(f'{ENDPOINT}branch/admin', params = params, headers = {'Authorization': token}).text)


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
		response = json.loads(requests.get(ENDPOINT+'category/admin', params = params, headers = {'Authorization': token}).text)
		return response


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
		data = '{\n  \"name\": {\n    \"en\": \"'+raw[2]+'\",\n    \"ru\": \"'+raw[1]+'\",\n    \"uz\": \"'+raw[0]+'\"\n  }\n}'
		if update:
			response = requests.put(f'{ENDPOINT}category/admin/{category_id}', data = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})
		else:
			response = requests.post(ENDPOINT+'category/admin', data = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def createBranch(token, request, branch_id = None, update = False):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
		if update:
			if 'image' in request.FILES:
				data = '{\n    "addressId": 1,\n    "capacity": '+request.POST['capacity']+',\n    "contacts": "'+request.POST['phone']+'",\n    "deletedImages": [\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/23e0d1ea-d9d3-4736-97e5-23d8c895d205Screen+Shot+2022-09-16+at+12.39.36.png?alt=media",\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/f736f58d-8f19-40d1-a3c8-7a22691d8d39Screen+Shot+2022-09-16+at+12.39.39.png?alt=media",\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/ffca292b-3032-4728-9c32-7384d01a13a6Screen+Shot+2022-09-16+at+12.39.41.png?alt=media"\n    ],\n    "information": {\n     "uz": {\n        "lang": "uz",\n        "text": "'+request.POST['name_uz']+'"\n      },\n      "ru": {\n        "lang": "ru",\n        "text": "'+request.POST['name_ru']+'"\n      },\n      "eng": {\n        "lang": "eng",\n        "text": "'+request.POST['name_en']+'"\n      }\n    },\n    "target": "'+request.POST['target']+' "\n  }'
				image = request.FILES['image']
				image.open(mode = 'rb')
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=images; filename=branch.jpg\r\nContent-Type: image/jpeg\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}branch/admin/{branch_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
				image.close()
			else:
				data = '{\n    "addressId": 1,\n    "capacity": '+request.POST['capacity']+',\n    "contacts": "'+request.POST['phone']+'",\n    "deletedImages": [\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/23e0d1ea-d9d3-4736-97e5-23d8c895d205Screen+Shot+2022-09-16+at+12.39.36.png?alt=media",\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/f736f58d-8f19-40d1-a3c8-7a22691d8d39Screen+Shot+2022-09-16+at+12.39.39.png?alt=media",\n      "https://firebasestorage.googleapis.com/v0/b/collectin-3959d.appspot.com/o/ffca292b-3032-4728-9c32-7384d01a13a6Screen+Shot+2022-09-16+at+12.39.41.png?alt=media"\n    ],\n    "information": {\n     "uz": {\n        "lang": "uz",\n        "text": "'+request.POST['name_uz']+'"\n      },\n      "ru": {\n        "lang": "ru",\n        "text": "'+request.POST['name_ru']+'"\n      },\n      "eng": {\n        "lang": "eng",\n        "text": "'+request.POST['name_en']+'"\n      }\n    },\n    "target": "'+request.POST['target']+' "\n  }'
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}'.encode(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}branch/admin/{branch_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})

		else:
			image = request.FILES['image']
			image.open(mode = 'rb')
			data = '{\n    "addressId": 1,\n    "capacity": '+request.POST['capacity']+',\n    "contacts": "'+request.POST['phone']+'",\n    "information": {\n     "uz": {\n        "lang": "uz",\n        "text": "'+request.POST['name_uz']+'"\n      },\n      "ru": {\n        "lang": "ru",\n        "text": "'+request.POST['name_ru']+'"\n      },\n      "eng": {\n        "lang": "eng",\n        "text": "'+request.POST['name_en']+'"\n      }\n    },\n    "target": "'+request.POST['target']+' "\n  }'
			data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=request;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=images; filename=branch.jpg\r\nContent-Type: image/jpeg\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
			response = requests.post(ENDPOINT+'branch', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
			image.close()


	@staticmethod
	def createSubCategory(token, raw, category_id = None, update = False):
		data = '{\n  \"name\": {\n    \"en\": \"'+raw['name_en']+'\",\n    \"ru\": \"'+raw['name_ru']+'\",\n    \"uz\": \"'+raw['name_uz']+'\"\n  },\n  \"parentCategoryId\": '+raw['parent']+'\n}'
		if update:
			response = requests.put(f'{ENDPOINT}category/admin/{category_id}', data = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})
		else:
			response = requests.post(ENDPOINT+'category/admin', data = data.encode(), headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})


	@staticmethod
	def deleteProduct(token, product_id):
		response = requests.delete(ENDPOINT+'product/'+str(product_id), headers = {'Authorization': token})


	@staticmethod
	def deleteCategory(token, category_id):
		response = requests.delete(ENDPOINT+'category/admin/'+str(category_id), headers = {'Authorization': token})


	@staticmethod
	def deleteBranch(token, branch_id):
		response = requests.delete(ENDPOINT+'branch/admin/'+str(branch_id), headers = {'Authorization': token})


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