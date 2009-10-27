from django import forms

from models import Moniton


class SubscribeForm(forms.ModelForm):
    """
    Form for subscribing to monitor.
    """
    class Meta(object):
        model = Moniton
        exclude = ['registered', 'uuid', 'created_at', 'updated_at']
