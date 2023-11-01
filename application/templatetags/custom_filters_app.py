from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def pow(value, pow):
    return value**pow




forbidden_words = ['content', 'second', 'important']
@register.filter
def replace_letters(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + '*' * (len(word)-2) + word[-1])
        else:
            result.append(word)
    return ' '.join(result)


