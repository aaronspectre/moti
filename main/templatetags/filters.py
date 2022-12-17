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
	print('Timestamp:', timestamp)
	return datetime.fromtimestamp(timestamp / 1000).strftime('%d %b, %H:%M')


@register.filter
def safeorder(order):
	return json.dumps(order)


@register.filter
def paid(p):
	return 'Да' if p else 'Нет'


@register.filter
def available(p):
	return 'Доступно' if p else 'Не доступно'