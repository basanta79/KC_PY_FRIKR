from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from photos.models import Photo


def latest_photos(request):
    # Recuperar las últimas fotos de la base de datos
    photos = Photo.objects.all().order_by('-modification_date')


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
