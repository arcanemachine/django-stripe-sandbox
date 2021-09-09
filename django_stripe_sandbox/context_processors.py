from django.conf import settings


def context_processors(request):
    return {'PROJECT_NAME': settings.PROJECT_NAME,
            'DEBUG_MODE': settings.DEBUG,
            'STATIC_URL': settings.STATIC_URL}
