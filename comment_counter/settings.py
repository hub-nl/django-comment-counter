from django.conf import settings

COMMENT_COUNTER_CACHE_TIMEOUT = getattr(settings, 'COMMENT_COUNTER_CACHE_TIMEOUT', 60*60*24*7)
