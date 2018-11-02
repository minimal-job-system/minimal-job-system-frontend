from django import template

from job_system_frontend import settings

register = template.Library()


@register.simple_tag
def app_title():
    return settings.APP_TITLE

@register.simple_tag
def app_icon():
    return settings.APP_ICON
