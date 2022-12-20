import json
from django import template
from datetime import datetime

register = template.Library()


@register.filter
def get_user_role(roles):
	if 'ADMIN' in roles:
		return 'secret'
	elif 'MANAGER' in roles:
		return 'police-tie'
	elif 'OPERATOR' in roles:
		return 'astronaut'
	else:
		return 'bounty-hunter'


@register.filter
def format_data(data):
	return json.dumps(data)


@register.filter
def todate(timestamp):
	return datetime.fromtimestamp(timestamp / 1000).strftime('%a %b %d %Y').title()


@register.filter
def delivery(date):
	try:
		if date == 'null':
			return 'Не определен'

		return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f').strftime('%b %d %Y, %H:%M').title()
	except Exception as error:
		return 'Не определен'


@register.filter
def safeorder(order):
	return json.dumps(order)


@register.filter
def paid(p):
	return 'Да' if p else 'Нет'


@register.filter
def available(p):
	return 'Доступно' if p else 'Не доступно'