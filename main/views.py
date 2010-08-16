from datetime import datetime

from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from crime.models import Crime


def index(request, template_name='main/index.html'):
    """
    Index page.
    """
    if request.method == 'GET':
        crimes = Crime.objects.filter(is_removed=False).order_by('-created_at')[:500]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'crimes': crimes,
        'crime_total': Crime.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)

def recent_updated(request, template_name='main/recent_updated.html'):
    """
    Return crime reports sort by recent updated.
    """
    if request.method == 'GET':
        crimes = Crime.objects.filter(is_removed=False).order_by('-updated_at')[:200]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'crimes': crimes,
        'crime_total': Crime.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)

def recent_commented(request, template_name='main/recent_commented.html'):
    """
    Return crime reports sort by recent commented.
    """
    if request.method == 'GET':
        # Hack to get recent commented. Getting all recent comments,
        # get the crime object id, and remove duplicates. Then retrive crime instances
        # using the ids.
        # Probably better approach is to capture comment stats thru Comments signals.

        ids = Comment.objects.all().values_list('object_pk', flat=True).order_by('-submit_date')[:500]
        ids = reduce(lambda l, x: int(x) not in l and l.append(int(x)) or l, ids, [])
        crime_dict = Crime.objects.in_bulk(ids[:200])
        crimes = [crime_dict[id] for id in ids if not crime_dict[id].is_removed]
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'crimes': crimes,
        'crime_total': Crime.objects.count(),
        'now': datetime.now(),
    })
    return render_to_response(template_name, context)
