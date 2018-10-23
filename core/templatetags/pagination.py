#coding=utf-8

from django.template import Library

register = Library()

@register.inclusion_tag('pagination.html')
def pagination(request,paginator,page_obj):
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['pag_obj'] = page_obj
    getrvars = request.GET.copy()

    if 'page' in getrvars:
        del getrvars['page']
    if len(getrvars) > 0:
        context['getvars'] = '&{0}'.format(getrvars.urlencode())
    else:
        context['getvars'] = ''

    return context