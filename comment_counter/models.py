from django.core.cache import cache
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.comments import get_model
from django.contrib.comments.signals import comment_was_posted, comment_was_flagged
from comment_counter.utils import get_cache_key_from_comment


@receiver(comment_was_posted)
def increment_counter(sender, comment, **kwargs):
    if getattr(comment, "is_public", True):
        key = get_cache_key_from_comment(comment)
        try:
            cache.incr(key)
        except ValueError:
            pass

@receiver(comment_was_flagged)
def decrement_counter_flagged(sender, flag, comment, **kwargs):
    if flag.flag == flag.MODERATOR_DELETION and getattr(comment, "is_public", True):
        key = get_cache_key_from_comment(comment)
        try:
            cache.decr(key)
        except ValueError:
            pass

@receiver(pre_delete, sender=get_model())
def decrement_counter_post_save(sender, instance, **kwargs):
    if getattr(instance, "is_public", True) and not getattr(instance, "is_removed", False):
        key = get_cache_key_from_comment(instance)
        try:
            cache.decr(key)
        except ValueError:
            pass
