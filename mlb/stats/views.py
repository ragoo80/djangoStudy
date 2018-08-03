# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


from django.http import Http404, HttpResponse
from django.template import Context, loader, RequestContext, Template

from django.utils._os import safe_join







# print settings.TEMPLATES[0]['DIRS'][0]

cureentApp = 'stats/'

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.BASE_DIR+'/templates/', name)
        print 'file_path: ', file_path
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path): raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def index(request, slug='index'):
    file_name = cureentApp + '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'STATIC_URL' : settings.STATIC_URL
    }
    return render(request, file_name, context)

    # template = loader.get_template(cureentApp + 'index.html')
    # context = {
    #     'con_test' : 'con_test_value',
    #     'STATIC_URL' : settings.STATIC_URL
    # }
    # return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")

def sub(request):
    template = loader.get_template(cureentApp+'sub.html')
    context = {
        'con_test' : 'con_test_value',
        'STATIC_URL' : settings.STATIC_URL
    }
    return HttpResponse(template.render(context), content_type="text/html; charset=UTF-8")
