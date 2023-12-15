from django import template

register = template.Library()

@register.filter
def split_string(value, delimiter=","):
    return value.split(delimiter)

@register.filter
def zip_list(list1,list2): 
    return zip(list1,list2)