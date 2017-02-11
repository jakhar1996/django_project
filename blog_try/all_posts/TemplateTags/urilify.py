from urllib import qoute_plus
from django import template

register = template.library()

@register.filter
def urilify(value):
	return qoute_plus(value)
