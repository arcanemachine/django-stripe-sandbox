from pprint import pformat
from django import template

register = template.Library()


@register.filter('pretty_print')
def pretty_print(value):
    """Convert a JSON value to a pretty-printed format"""
    return pformat(value, indent=2, sort_dicts=False)
