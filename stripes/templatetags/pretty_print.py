from pprint import pformat
from django import template

register = template.Library()


@register.filter('pretty_print')
def pretty_print(obj):
    """Convert a JSON value to a pretty-printed format"""
    return pformat(obj, indent=2, sort_dicts=False)
