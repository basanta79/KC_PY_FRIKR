from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from photos.forms import PhotoForm
from photos.models import Photo


def latest_photos(request):
    # Recuperar las últimas fotos de la base de datos
    photos = Photo.objects.filter(visibility=Photo.PUBLIC).all().order_by('-modification_date')


    # definir el contexto par pasarle las fotos a la plantilla
    context = { 'latest_photos': photos[:3]}
    print(photos)

    # crear una respuesta html
    html = render(request, 'photos/latest.html', context)

    # devolver la respuesta http
    return HttpResponse(html)


def photo_detail(request, pk):
    # Recuperar la foto seleccionada de la base de datos
    # try:
    #     photo = Photo.objects.get(pk=pk)
    # except Photo.DoesNotExist:
    #     return HttpResponseNotFound('Photo does not exist')
    # Lo que esta comentado arriba es lo mismo que la linia de abajo
    photo = get_object_or_404(Photo, pk=pk)

    # Crear un contexto para pasar la información a la plantilla
    context = {'photo': photo}

    # Renderizar la plantilla
    html = render(request, 'photos/detail.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)


def new_photo(request):
    if request.method=='POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save()
            messages.success(request, 'Foto creada correctamente con id {0}'.format(new_photo.pk))
            form = PhotoForm()
    else:
        form = PhotoForm()
    context = {'form': form}
    return render(request, 'photos/new.html', context)
