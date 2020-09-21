from django import template

register=template.Library()

@register.filter
def modulo(num,val):
    print("first",num,val)
    return num % val


@register.filter
def moduloend(num,val):
    val=num+4
    print("end",num,val)
    return num % val



@register.filter
def pages(num,val):
    return num/val