from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from hobbie.models import Card, MyTrack
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    tasks = Card.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'hobbie/index.html', context)


def mymap(request):
    return render(request, 'hobbie/mao.html', {'user': request.user})


@csrf_exempt
def savetrack(request):
    if request.is_ajax():
        if request.method == 'POST':
           #print(json.loads(request.body.decode('utf-8')))
            trackdata = json.loads(request.body.decode('utf-8'))
            mt = MyTrack()
            mt.username = trackdata['user']
            mt.track = json.dumps(trackdata['track'])
            mt.trackname = trackdata['name']
            mt.save()
            print('saved!')
    return HttpResponse("OK")


def gettrack(request):
    user = request.user
    tracks = MyTrack.objects.filter(username=user).order_by("created_date")
    return render(request, 'hobbie/gettrack.html', {'tracks': tracks})
