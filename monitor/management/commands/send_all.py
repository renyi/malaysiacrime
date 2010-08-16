import logging, smtplib
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.template import Context
from django.template.loader import get_template

from crime.models import Crime
from monitor.models import Moniton


class Command(BaseCommand):
    """
    Called by cron job to iterate thru all monitons and send emails accordingly.
    Only check crime reports for the last 24 hours.
    """
    def handle(self, *args, **options):
        # Get crime reports in the last 24 hours.
        now = datetime(*args) if args else datetime.now()
        past = now - timedelta(1)
        latest_crimes = Crime.objects.filter(is_removed=False, created_at__gt=past)

        # Iterate all monitons. Send emails on crimes that are of interest.
        for m in Moniton.objects.all():
            crimes = [x for x in latest_crimes if m.top >= x.lat and m.bottom <= m.right >= x.lng and m.left <= x.lng]
            if crimes:
                try:
                    send_mail('[Malaysia Crime] Notification of Crimes',
                        get_template('monitor/notification_email.txt').render(Context({'uuid': m.uuid, 'crimes': crimes})),
                        'noreply@malaysiacrime.com', [m.email])
                except smtplib.SMTPException, e:
                    logging.error(e)
