from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

CATEGORY_SYMBOLS = {
   'fin': '$',
   'cul': '&',
   'sci': '#'
}


@register.filter()
def cat(value, code='fin'):
   postfix = CATEGORY_SYMBOLS[code]
   return f'{value} {postfix}'



word = ['the', 'central', 'making']#I tried, but it is still censoring only the last word in the list


@register.filter
@stringfilter
def censor(value):
    for w in word:
      val = value.replace(w[1:], '*' * len(w[1:]))
    return val

#val = value.replace(w, w[0] + '*' * len(w[1:]))