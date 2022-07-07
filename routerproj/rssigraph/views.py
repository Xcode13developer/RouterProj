import datetime
from django.shortcuts import render

from rssigraph.models import Point
from rssigraph.router import store

# Create your views here.
def index(request):
    #get all points within the hour
    hour = datetime.datetime.now().hour
    pointsArray = []
    points = Point.objects.filter(date="%d / %d . %d" % (datetime.datetime.now().month, datetime.datetime.now().day, hour))
    for point in points:
        pointsArray.append([point.xPerHour, point.RSSIy, point.RSRPy])
    if pointsArray == []:
        pointsArray = [[0, 0, 0]]
    return render(request, 'index.html', {'points': pointsArray})

