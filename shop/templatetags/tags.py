from django import template

register=template.Library()

@register.filter
def modulo(num,val):
    print(num,val)
    return num % val

@register.filter
def pages(num,val):
    return num/val