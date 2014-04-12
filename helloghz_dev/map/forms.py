from django import forms


class helloForm(forms.Form):
    vid = forms.CharField(max_length=20)
    lat = forms.FloatField()
    long = forms.FloatField()


class HelloForm2(forms.Form):

    class Video(forms.Form):
        videoId = forms.CharField(max_length=20)
        latitude = forms.FloatField()
        longitude = forms.FloatField()