from django import forms

from models import Moniton


class SubscribeForm(forms.ModelForm):
    """
    Form for subscribing to monitor.
    """
    lat    = forms.FloatField(widget=forms.HiddenInput())
    lng    = forms.FloatField(widget=forms.HiddenInput())
    top    = forms.FloatField(widget=forms.HiddenInput())
    right  = forms.FloatField(widget=forms.HiddenInput())
    bottom = forms.FloatField(widget=forms.HiddenInput())
    left   = forms.FloatField(widget=forms.HiddenInput())
    zoom   = forms.IntegerField(widget=forms.HiddenInput())

    class Meta(object):
        model = Moniton
        exclude = ['registered', 'uuid', 'created_at', 'updated_at']
