from django.http import HttpResponse
from django.template import loader
from .models import Album,Song

def mainWebSite(request):
    return HttpResponse("<h1> Hey Welcome To Sonika's Site </h1>")

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }
    return HttpResponse(template.render(context, request))

def detail(request , album_id):
    album = Album.objects.get(pk=album_id)
    template = loader.get_template('music/details.html ')
    context = {'album': album}
    return HttpResponse(template.render(context, request))
