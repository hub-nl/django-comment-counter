import hashlib
from django.utils.encoding import smart_str


def get_counter_cache_key(site_id, content_type_id, object_pk):
    if object_pk is None:
        raise ValueError("object_pk is None")

    try:
        object_pk = int(object_pk)
    except (TypeError, ValueError):
        md5 = hashlib.md5(smart_str(object_pk))
        object_pk = md5.hexdigest()

    return "django:comments:counter_cache:%d_%d_%s" % (site_id, content_type_id, object_pk)


def get_cache_key_from_comment(comment):
    return get_counter_cache_key(comment.site_id, comment.content_type_id, comment.object_pk)
