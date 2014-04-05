from django import forms

class helloForm(forms.Form):
    vid = forms.CharField(max_length=20)
    lat = forms.FloatField()
    long = forms.FloatField()

