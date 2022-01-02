DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += [
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
