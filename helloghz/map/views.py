# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from map.models import Point
from map.forms import helloForm
from urlparse import urlparse



#index just returns list of points for javascript to map
def index(request):
    returnlist = Point.objects.all()
    context = {'returnlist': returnlist}

    return render(request, 'map/index.html', context)

#Lets users add a video to the database to be mapped
def sayhello(request):

    if request.method == 'POST': # If the form has been submitted...
        form = helloForm(request.POST) # A form bound to the POST data
        if canPostData(request.POST): # All validation rules pass

            videoId = getVideoId(form.cleaned_data['full_url'])

            newPoint = Point(vid=videoId, lat=form.cleaned_data['lat'], long=form.cleaned_data['long'])

            newPoint.save()
            # ...
            return HttpResponseRedirect('/map/') # Redirect after POST
    else:
        form = helloForm() # An unbound form

    return render(request, 'map/sayhello.html', {
        'form': form,
    })

def getVideoId(fullUrl):
    """
    returns video id when given a youtube url
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(fullUrl)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

def canPostData(postedData):
    form = helloForm(postedData)
    if not form.is_valid():
        return False
    videoId = str(getVideoId(form.cleaned_data['full_url']))
    if videoId is None:
        return False

    return True
