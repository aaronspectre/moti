import json
import requests


ENDPOINT = 'https://moti-panasian.herokuapp.com/api/v1/'


class Swagger:
	@staticmethod
	def auth(username, password):
		data = {'phonenumber': username, 'password': password}
		response = json.loads(requests.post(ENDPOINT+'auth/login_admin', json = data).text)
		return response


	@staticmethod
	def filter(status, token):
		params = {
			'offset': 0,
			'status': status,
			'sort.sorted': 'true',
			'paged': 'false',
			'unpaged': 'true'
		}
		response = json.loads(requests.get(ENDPOINT+'order/by_status', params = params, headers = {'Authorization': token}).text)
		return response['data']