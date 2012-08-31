from datetime import datetime
from uuid import uuid1

from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, RequestContext, Template
from django.template.loader import get_template

from models import Moniton
from forms import SubscribeForm


def subscribe(request, form_class=SubscribeForm, template_name='monitor/subscribe.html'):
    """
    Subscribe to monitor an area.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            moniton = form.save(commit=False)
            moniton.uuid = uuid1().hex # uuid used for unsubscribe.
            moniton.save()

            # Send notification email.
            try:
                send_mail(
                    'Malaysia Crime Monitor subscription',
                    get_template('monitor/subscribe_email.txt').render(Context({'uuid': moniton.uuid})),
                    'noreply@malaysiacrime.com', [moniton.email])
            except smtplib.SMTPException, e:
                pass # Email sending is unreliable service anyway. So don't bother handling it.

            return redirect('monitor-subscribe-done')
    elif request.method == 'GET':
        form = form_class()
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'form': form,
    })
    return render_to_response(template_name, context)

def unsubscribe(request, uuid, template_name='monitor/unsubscribe.html'):
    """
    Process unsubscribe.
    """
    moniton = get_object_or_404(Moniton, uuid=uuid)

    if request.method == 'POST':
        moniton.delete()
        return redirect('monitor-unsubscribe-done')
    elif request.method == 'GET':
        pass
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'moniton': moniton,
    })
    return render_to_response(template_name, context)

def information(request, uuid, template_name='monitor/information.html'):
    """
    Show the monitoring area.
    """
    if request.method == 'GET':
        moniton = get_object_or_404(Moniton, uuid=uuid)
    else:
        return HttpResponseRedirect(request.path)

    context = RequestContext(request, {
        'moniton': moniton,
    })
    return render_to_response(template_name, context)
