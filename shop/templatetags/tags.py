from django import template

register=template.Library()

@register.filter
def modulo(num,val):
    return num % val


@register.filter
def returnitem(l, i):
    try:
        return l[i]
    except:
        return None

@register.filter
def pages(num,val):
    return num/val