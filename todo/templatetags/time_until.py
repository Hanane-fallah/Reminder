from datetime import datetime, timezone

from django import template

register = template.Library()


def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


register.filter('cut', cut)
register.filter('lower', lower)


@register.filter
def calc_time(due_date):
    if due_date:
        # due_date = datetime.strptime(due_date, '%b %d %Y %I:%M%p')
        now = datetime.now(timezone.utc)
        if (due_date - now).seconds > 0 and (due_date - now).days >= 0:
            return due_date - now

    return False


