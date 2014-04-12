# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from map.models import Point
from map.forms import helloForm


#index just returns list of points for javascript to map
def index(request):
    returnlist = Point.objects.all()
    context = {'returnlist': returnlist}

    return render(request, 'map/index.html', context)

#Lets users add a video to the database to be mapped
def sayhello(request):

    if request.method == 'POST': # If the form has been submitted...
        form = helloForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            newPoint = Point(vid=form.cleaned_data['vid'],lat=form.cleaned_data['lat'],long=form.cleaned_data['long'])

            newPoint.save()
            # ...
            return HttpResponseRedirect('/map/') # Redirect after POST
    else:
        form = helloForm() # An unbound form

    return render(request, 'map/sayhello.html', {
        'form': form,
    })
