from django import template

from job_system_frontend import settings

register = template.Library()


@register.simple_tag
def app_title():
    return settings.APP_TITLE


@register.simple_tag
def app_icon():
    return settings.APP_ICON


@register.simple_tag
def only_owner_can_stop_job():
    return settings.ONLY_OWNER_CAN_STOP_JOB
