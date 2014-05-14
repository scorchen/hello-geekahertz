from django import forms

class helloForm(forms.Form):
    full_url = forms.URLField(required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    lat = forms.FloatField(required=True)
    long = forms.FloatField(required=True)
    #vTitle = forms.CharField(max_length=120)
    #vDescription = forms.CharField(max_length=5000)
    address = forms.CharField(max_length=100,
                              required=True,
                              initial="Salt Lake City, UT",
                              widget=forms.TextInput(attrs={"class": "form-control"})

    )
