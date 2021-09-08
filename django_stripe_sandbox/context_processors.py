from django.conf import settings


def helpers(request):
    return {'DEBUG_MODE': settings.DEBUG,
            'PROJECT_NAME': settings.PROJECT_NAME,
            'STATIC_URL': settings.STATIC_URL}
