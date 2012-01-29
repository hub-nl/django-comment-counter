from django import template
from django.contrib.comments.templatetags.comments import (
    get_comment_list,
    get_comment_form,
    render_comment_form,
    comment_form_target,
    get_comment_permalink,
    render_comment_list,
)
from comment_counter.templatetags.comment_count import get_cached_comment_count


register = template.Library()


def get_comment_count(*args, **kwargs):
    return get_cached_comment_count(*args, **kwargs)

register.tag(get_comment_count)
register.tag(get_comment_list)
register.tag(get_comment_form)
register.tag(render_comment_form)
register.simple_tag(comment_form_target)
register.simple_tag(get_comment_permalink)
register.tag(render_comment_list)
