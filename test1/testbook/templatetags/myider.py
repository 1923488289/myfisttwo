from django import template

register = template.Library()


@register.filter
def myder(a):
    if a == 0:
        return '男'
    else:
        return '女'


@register.filter
def value1(x):
    if x == 0:
        return 'men'
    else:
        return 'women'
