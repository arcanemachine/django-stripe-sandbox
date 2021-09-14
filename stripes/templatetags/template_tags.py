import logging
import re
from django import template
from django.conf import settings
from pprint import pformat

register = template.Library()


@register.filter('pretty_print')
def pretty_print(value):
    """Convert a JSON value to a pretty-printed format"""
    return pformat(value, sort_dicts=False)


@register.simple_tag(takes_context=True)
def view_name_as_page_title(context):
    view_name = context['request'].resolver_match.func.__name__

    # add spaces before capital letters
    spaced_view_name = re.sub(r"(\w)([A-Z])", r"\1 \2", view_name)

    # remove ' View' from the result
    if spaced_view_name[-5:] == ' View':
        spaced_view_name = spaced_view_name[:-5]

    return spaced_view_name


@register.simple_tag(takes_context=True)
def set_breakpoint(context, *args):
    """
Set breakpoints in the template for easy examination of the context,
or any variables of your choice.

Usage:
    {% load breakpoint %}
    {% set_breakpoint %}
          - or -
    {% set_breakpoint your_variable your_other_variable %}

- The context is always accessible in the pdb console as a dict 'context'.

- Custom variables can be accessed as vars[i] in the pdb console.
    - vars[0] is your_variable, vars[1] is your_other_variable
    """

    vars = [arg for arg in locals()['args']]  # noqa F841

    if settings.DEBUG:
        breakpoint()
    else:
        # log warning if breakpoint detected when DEBUG is False
        logger = logging.getLogger(__name__)
        view_name = context['view'].__class__.__name__
        logger.warning("\nWarning! "
                       f"The template in {view_name} contains a breakpoint!\n")
