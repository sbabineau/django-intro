from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
import models


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def front_view(request):
    return render(request, 'photoshare/front.html')


def login_view(request):
    request.next = 'photoshare/home'
    return login(
        request,
        template_name='registration/login.html',)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required
def home_view(request):
    albums = models.Album.objects.filter(owner=request.user).all()
    context = {'albums': albums}
    return render(request, 'photoshare/home.html', context)


@login_required
def album_view(request, album):
    album = models.Album.objects.get(pk=album)
    context = {'album': album}
    return render(request, 'photoshare/album.html', context)


@login_required
def photo_view(request, photo):
    photo = models.Photo.objects.get(pk=photo)
    context = {'photo': photo}
    return render(request, 'photoshare/photo.html', context)


@login_required
def tag_view(request, tag):
    photos = models.Photo.objects.filter(owner=request.user).filter(tags=tag).all()
    context = {'photos': photos, 'tag': tag}
    return render(request, 'photoshare/tag.html', context)


def add_photo_view(request):
    pass
