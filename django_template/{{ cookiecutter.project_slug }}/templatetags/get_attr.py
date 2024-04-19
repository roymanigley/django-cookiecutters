from django.template import Library

register = Library()


@register.filter('get_attr')
def get_attr(value, key):
    result = None
    if value is not None:
        if hasattr(value, key):
            result = getattr(value, key)
        elif type(value) is dict and key in value.keys():
            result = value[key]
    return result if result is not None else ''
