import logging
from django import template
from django.conf import settings

register = template.Library()


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
