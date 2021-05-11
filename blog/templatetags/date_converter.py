from django import template

register = template.Library()


@register.filter
def dateConverter(values):
    return values.lower()
