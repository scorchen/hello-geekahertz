from django.core.management.base import BaseCommand, CommandError
from map.models import Point
import urllib
import simplejson

class Command(BaseCommand):
    args = 'no args'
    help = 'pulls youtube json and updates lat/long if needed'

    def handle(self, *args, **options):
        mypoints = Point.objects.all()
        for mypoint in mypoints:
             id = mypoint.vid
             url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CrecordingDetails&id=' + mypoint.vid + '&key=AIzaSyC5uDjEOvf_uKgsD-Gbzp-DlhWPSGsdsS0'
             json = simplejson.load(urllib.urlopen(url))
             try:
                lat = json['items'][0]['recordingDetails']['location']['latitude']
             except:
                lat = ''
             try:
                long = json['items'][0]['recordingDetails']['location']['longitude']
             except:
                long = ''

             if (lat != '' and long != ''):
                if(lat != mypoint.lat or lat != mypoint.long):
                    mypoint.lat = lat
                    mypoint.long = long
                    mypoint.save()

