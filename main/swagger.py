import json
import requests
import mimetypes


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
		response = json.loads(requests.get(ENDPOINT+'user/all', params = params, headers = {'Authorization': token}).text)
		return response['content']


	@staticmethod
	def update_user(token, data, user_id):
		data = '{\n  "name": "'+data['name']+'",\n  "role": "'+data['role']+'"\n}'
		response = requests.put(f'{ENDPOINT}user/{user_id}', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def change_password(token, data):
		data = '{\n  "oldPassword": "'+data['old']+'",\n  "newPassword": "'+data['new']+'"\n}'
		user = json.loads(requests.get(ENDPOINT+'user/me', headers = {'Authorization': token}).content)
		response = requests.put(f'{ENDPOINT}user/change-password/{user["id"]}', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def updateOrder(token, status, order_id):
		data = '{\n    \"status\":\"'+status+'\"\n}'
		response = requests.put(f'{ENDPOINT}order/admin/{order_id}', data = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})


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
		return response['content']


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
			data = '{\n  "available": '+request.POST['available']+',\n  "categoryId": '+request.POST['category']+',\n  "code": "'+request.POST['code']+'",\n  "description": {\n    "en": "'+request.POST['desc_en']+'",\n    "ru": "'+request.POST['desc_ru']+'",\n    "uz": "'+request.POST['desc_uz']+'"\n  },\n  "discount": '+str(request.POST['discount'])+',\n  "name": {\n    "en": "'+request.POST['name_en']+'",\n    "ru": "'+request.POST['name_ru']+'",\n    "uz": "'+request.POST['name_uz']+'"\n  },\n  "price": '+str(request.POST['price'])+',\n  "readyTime": '+request.POST['time']+'\n}'
			if 'image' in request.FILES:
				image = request.FILES['image']
				image.open(mode = 'rb')
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=product;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename={image.name}\r\nContent-Type: {image.content_type}\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}product/admin/{product_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
				image.close()
			else:
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=product\r\nContent-Type: application/json\r\n\r\n{data}'.encode(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}product/admin/{product_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
		else:
			image = request.FILES['image']
			image.open(mode = 'rb')
			data = '{\n  "available": '+request.POST['available']+',\n  "categoryId": '+request.POST['category']+',\n  "code": "'+request.POST['code']+'",\n  "description": {\n    "en": "'+request.POST['desc_en']+'",\n    "ru": "'+request.POST['desc_ru']+'",\n    "uz": "'+request.POST['desc_uz']+'"\n  },\n  "discount": '+str(request.POST['discount'])+',\n  "name": {\n    "en": "'+request.POST['name_en']+'",\n    "ru": "'+request.POST['name_ru']+'",\n    "uz": "'+request.POST['name_uz']+'"\n  },\n  "price": '+str(request.POST['price'])+',\n  "readyTime": '+request.POST['time']+'\n}'
			data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=product;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename={image.name}\r\nContent-Type: {image.content_type}\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
			response = requests.post(ENDPOINT+'product/admin', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
			image.close()


	@staticmethod
	def createCategory(token, raw, category_id = None, update = False):
		data = '{\n  \"name\": {\n    \"en\": \"'+raw[2]+'\",\n    \"ru\": \"'+raw[1]+'\",\n    \"uz\": \"'+raw[0]+'\"\n  }\n}'
		if update:
			response = requests.put(f'{ENDPOINT}category/admin/{category_id}', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})
		else:
			response = requests.post(ENDPOINT+'category/admin', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def createBranch(token, request, branch_id = None, update = False):
		boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
		if update:
			if 'image' in request.FILES:
				image = request.FILES['image']
				image.open(mode = 'rb')
				data = '{\n  "address": {\n    "district": "'+request.POST['district']+'",\n    "name": "'+request.POST['address_name']+'",\n    "street": "'+request.POST['street']+'",\n    "latitude": '+request.POST['latitude']+',\n    "longitude": '+request.POST['longitude']+'\n  },\n  "capacity": '+request.POST['capacity']+',\n  "contacts": "'+request.POST['phone']+'",\n  "information": {\n    "uz": "'+request.POST['name_uz']+'",\n    "ru": "'+request.POST['name_ru']+'",\n    "en": "'+request.POST['name_en']+'"\n  },\n  "target": "'+request.POST['target']+'"\n}'
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=branch;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename={image.name}\r\nContent-Type: {image.content_type}\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}branch/admin/{branch_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
				image.close()
			else:
				data = '{\n  "address": {\n    "district": "'+request.POST['district']+'",\n    "name": "'+request.POST['address_name']+'",\n    "street": "'+request.POST['street']+'",\n    "latitude": '+request.POST['latitude']+',\n    "longitude": '+request.POST['longitude']+'\n  },\n  "capacity": '+request.POST['capacity']+',\n  "contacts": "'+request.POST['phone']+'",\n  "information": {\n    "uz": "'+request.POST['name_uz']+'",\n    "ru": "'+request.POST['name_ru']+'",\n    "en": "'+request.POST['name_en']+'"\n  },\n  "target": "'+request.POST['target']+'"\n}'
				data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=branch;\r\nContent-Type: application/json\r\n\r\n{data}'.encode(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
				response = requests.put(f'{ENDPOINT}branch/admin/{branch_id}', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})

		else:
			image = request.FILES['image']
			image.open(mode = 'rb')
			data = '{\n  "address": {\n    "district": "'+request.POST['district']+'",\n    "name": "'+request.POST['address_name']+'",\n    "street": "'+request.POST['street']+'",\n    "latitude": '+request.POST['latitude']+',\n    "longitude": '+request.POST['longitude']+'\n  },\n  "capacity": '+request.POST['capacity']+',\n  "contacts": "'+request.POST['phone']+'",\n  "information": {\n    "uz": "'+request.POST['name_uz']+'",\n    "ru": "'+request.POST['name_ru']+'",\n    "en": "'+request.POST['name_en']+'"\n  },\n  "target": "'+request.POST['target']+'"\n}'
			data = b''.join((f'--{boundary}\r\nContent-Disposition: form-data; name=branch;\r\nContent-Type: application/json\r\n\r\n{data}\r\n--{boundary}\r\nContent-Disposition: form-data; name=image; filename={image.name}\r\nContent-Type: {image.content_type}\r\n\r\n'.encode(), image.read(), b'\r\n--wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T--\r\n'))
			response = requests.post(ENDPOINT+'branch/admin', data = data, headers = {'Authorization': token, 'Content-Type': f'multipart/form-data; boundary={boundary}'})
			image.close()


	@staticmethod
	def createSubCategory(token, raw, category_id = None, update = False):
		data = '{\n  \"name\": {\n    \"en\": \"'+raw['name_en']+'\",\n    \"ru\": \"'+raw['name_ru']+'\",\n    \"uz\": \"'+raw['name_uz']+'\"\n  },\n  \"parentCategoryId\": '+raw['parent']+'\n}'
		if update:
			response = requests.put(f'{ENDPOINT}category/admin/{category_id}', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})
		else:
			response = requests.post(ENDPOINT+'category/admin', data = data.encode(), headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def deleteProduct(token, product_id):
		response = requests.delete(ENDPOINT+'product/admin/'+str(product_id), headers = {'Authorization': token})


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
	def update_fee(token, data):
		data = {
			'deliveryPayment': float(data['payment']),
			'price': float(data['price'])
		}
		response = requests.put(f'{ENDPOINT}fee', json = data, headers = {'Authorization': token, 'Content-Type': 'application/json'})


	@staticmethod
	def report(token):
		response = json.loads(requests.get(ENDPOINT+'report', headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def report_most_selling(token):
		response = json.loads(requests.get(ENDPOINT+'report/most-sell-products', headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def report_payment_methods(token):
		response = json.loads(requests.get(ENDPOINT+'report/sell-statistic', headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def report_last_30_orders(token):
		response = json.loads(requests.get(ENDPOINT+'report/last-30-orders', headers = {'Authorization': token}).text)
		return response


	@staticmethod
	def report_download(token, start, end):
		payload = '{\n    \"from\" : '+str(start)+',\n    \"to\" : '+str(end)+'\n}'
		headers = {'Authorization': token, 'Content-Type': 'application/json'}
		response = requests.post(ENDPOINT+'report/download-excel', data = payload, headers = headers)
		with open('report.xlsx', 'wb') as report:
			report.write(response.content)



if __name__ == '__main__':
	print('Swagger')