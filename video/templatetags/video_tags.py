from django import template


register = template.Library()


@register.filter
def get_tag(obj):
    if 'comics' in obj.tags:
        return 'comics'
    elif 'music' in obj.tags:
        return 'music'
    elif 'games' in obj.tags:
        return 'games'
    elif 'film' in obj.tags:
        return 'film'
    elif 'tv' in obj.tags:
        return 'tv'
    elif 'interactive' in obj.tags:
        return 'interactive'
    else:
        return 'extra'
