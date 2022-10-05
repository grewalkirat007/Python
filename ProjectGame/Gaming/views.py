from django.shortcuts import render
from django.http import HttpResponse
from .models import Game,Leadership,News,Players,Status,Update
from .form import gameForm

# Create your views here.
def getData(request):
    data = Game.objects.all()
    context = {
        'game_list':data
    }
    return render(request, "index.html", context)

def gamee(request):
    game = gameForm
    return render(request,'new.html',{'game':game})