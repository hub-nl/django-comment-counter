from django.core.cache import cache
from django import template
from django.conf import settings
from django.contrib.comments.templatetags.comments import CommentCountNode
from comment_counter.utils import get_counter_cache_key
from comment_counter.settings import DEFAULT_COUNTER_CACHE_TIMEOUT


register = template.Library()


class CachedCommentCountNode(CommentCountNode):
    """Insert a count of comments into the context."""
    def render(self, context):
        ctype, object_pk = self.get_target_ctype_pk(context)
        if not object_pk:
            context[self.as_varname] = 0
            return ''

        cache_key = get_counter_cache_key(settings.SITE_ID, ctype.id, object_pk)
        count = cache.get(cache_key)
        if count is None:
            qs = self.get_query_set(context)
            count = self.get_context_value_from_queryset(context, qs)
            cache.set(cache_key, count, DEFAULT_COUNTER_CACHE_TIMEOUT)

        context[self.as_varname] = count
        return ''


def get_cached_comment_count(parser, token):
    """
    Gets the comment count for the given params and populates the template
    context with a variable containing that value, whose name is defined by the
    'as' clause.

    Syntax is the same as for django's get_comment_count.
    """
    return CachedCommentCountNode.handle_token(parser, token)


register.tag(get_cached_comment_count)
