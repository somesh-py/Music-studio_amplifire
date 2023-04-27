from django.shortcuts import render,redirect
from .models import MusicReg
# Create your views here.


def index(request):
    song = MusicReg.objects.all()
    return render(request, 'allsongs.html', {'song': song})


def song(request, id):
    song = MusicReg.objects.get(id=id)
    return render(request, 'mainsong.html', {'song': song})


def registersongform(request):
    return render(request, 'songregister.html')


def registersong(request):
    if request.method == 'POST':
        name = request.POST['name']
        artist = request.POST['artist']
        relese_date = request.POST['relese_date']
        genre = request.POST['genre']
        audio = request.FILES.get('audio')
        image = request.FILES.get('image')
        duration = request.POST['duration']
        album = request.POST['album']

        MusicReg.objects.create(name=name, artist=artist, release_date=relese_date,
                                       genre=genre, audio=audio, image=image, duration=duration, album=album)
        return redirect('/')

