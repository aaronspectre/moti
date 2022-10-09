import json
from django import template

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