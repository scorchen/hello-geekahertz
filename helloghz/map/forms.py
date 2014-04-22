from django import forms

class helloForm(forms.Form):
    full_url = forms.URLField(min_length=30,
                              required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    lat = forms.FloatField(required=True)
    long = forms.FloatField(required=True)
    address = forms.CharField(max_length=100,
                              required=True,
                              initial="Salt Lake City, UT",
                              widget=forms.TextInput(attrs={"class": "form-control"})
    )
