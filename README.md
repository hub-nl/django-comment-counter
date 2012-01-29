This app caches comment count in a django project. It contains a replacement for `get_comment_count` template tag. 

Counters are stored in cache with long lifetime and are updated by signals. Custom comment backends and moderation are supported.

To enable this application add `comment_counter` to `INSTALLED_APPS` and replace `{% load comments %}` with `{% load comments_with_cache %}`. That's all.
