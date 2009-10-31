import django
from datetime import datetime

from django.core import mail
from django.core.management import call_command
from django.test import TestCase

from models import Moniton


class MonitonTestCase(TestCase):
    """
    Test operations for crime areas monitoring.
    """
    urls = 'monitor.urls'
    fixtures = ['monitor/fixtures/monitons.json', 'monitor/fixtures/crimes.json']

    def setUp(self):
        pass

    def test_get_subscribe(self):
        """
        Test accessing subscribe page.
        """
        response = self.client.get('/subscribe/')
        self.assertTemplateUsed(response, 'monitor/subscribe.html')

    def test_post_subscribe(self):
        """
        Test subscribing to monitor.
        """
        inputs = {
            'email': 'kegan@kegan.info',
            'top': 1.1234,
            'right': 1.1234,
            'bottom': 1.1234,
            'left': 1.1234,
            'zoom': 9,
        }
        response = self.client.post('/subscribe/', inputs)

        self.assertTrue(mail.outbox)
        self.assertEquals(mail.outbox[0].to, [inputs['email']])
        self.assertEquals(mail.outbox[0].subject, 'Malaysia Crime Monitor subscription')
        self.assertRedirects(response, '/subscribe/done/')

    def test_post_subscribe_email_invalid(self):
        """
        Test subscribing to monitor.
        """
        inputs = {
            'email': 'xxx',
            'top': 1.1234,
            'right': 1.1234,
            'bottom': 1.1234,
            'left': 1.1234,
            'zoom': 9,
        }
        response = self.client.post('/subscribe/', inputs, follow=True)
        self.assertFormError(response, 'form', 'email', 'Enter a valid e-mail address.')

    def test_get_unsubscribe_uuid_invalid(self):
        """
        Test getting unsubscription with invalid uuid.
        """
        response = self.client.get('/unsubscribe/%s/' % 'xxx')
        self.assertTemplateUsed(response, '404.html')

    def test_get_unsubscribe(self):
        """
        Test getting an unsubscription.
        """
        response = self.client.get('/unsubscribe/%s/' % '4ad2302c454311de8b3387c74347e6f7')
        self.assertTemplateUsed(response, 'monitor/unsubscribe.html')
        self.assertEquals(response.context['moniton'].email, 'zul@example.com')

    def test_post_unsubscribe_uuid_invalid(self):
        """
        Test unsubscription with invalid uuid.
        """
        response = self.client.post('/unsubscribe/%s/' % 'xxx')
        self.assertTemplateUsed(response, '404.html')

    def test_post_unsubscribe(self):
        """
        Test unsubscription.
        """
        response = self.client.post('/unsubscribe/%s/' % '5432a3fc49ff11de854c1730b0756f01', follow=True)
        self.assertTemplateUsed(response, 'monitor/unsubscribe_done.html')
        self.assertRaises(django.core.exceptions.ObjectDoesNotExist, Moniton.objects.get, email='leremy@example.com')

    def test_get_information(self):
        """
        Test showing the area of subscription.
        """
        response = self.client.get('/info/%s/' % '03619ac2453211de8c651fabc0151a16')
        self.assertTemplateUsed(response, 'monitor/information.html')
        self.assertEquals(response.context['moniton'], Moniton.objects.get(pk=1))

    # def test_monitor_initial_log_creation(self):
    #     """
    #     Test creating of first log, when not log data is available.
    #     """
    #     Log.objects.all().delete()
    #     call_command("send_all", '1238860800') # Timestamp for 2009-04-05.
    #     log = Log.objects.all().latest('created_at')
    #
    #     self.assertEquals(log.start, log.end)
    #
    # def test_monitor_subsequest_log_creation(self):
    #     """
    #     Test creating of subsequent log entry.
    #     """
    #     call_command("send_all", '1238860800') # Timestamp for 2009-04-05.
    #     log = Log.objects.all().latest('created_at')
    #
    #     self.assertEquals(log.start, datetime(2009, 04, 05, 0, 0))
    #     self.assertTrue(log.start < log.end)
    #
    # def test_monitor_notification(self):
    #     """
    #     Test the correctness of notifications.
    #     """
    #     call_command("send_all", '1238860800') # Timestamp for 2009-04-05.
    #
    #     self.assertEquals(len(mail.outbox), 2)
    #
    #     self.assertEquals(mail.outbox[0].to, ['confirm1@example.com'])
    #     self.assertNotEquals(mail.outbox[0].body.rfind('Terrible Crime Middle In Date'), -1)
    #     self.assertNotEquals(mail.outbox[0].body.rfind('Terrible Crime East'), -1)
    #
    #     self.assertEquals(mail.outbox[1].to, ['confirm2@example.com'])
    #     self.assertNotEquals(mail.outbox[1].body.rfind('Terrible Crime Middle In Date'), -1)
    #     self.assertNotEquals(mail.outbox[1].body.rfind('Terrible Crime West'), -1)

    def tearDown(self):
        pass


# Disabled TEMPLATE_DIRS so that custom templates would not intefere with tests.
from django.conf import settings
settings.TEMPLATE_DIRS = ()
