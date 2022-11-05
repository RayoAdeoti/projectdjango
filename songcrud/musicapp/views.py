# from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import is_valid_path
from musicapp.models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer
from .serializers import SongSerializer
from .serializers import LyricSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def index(request):
#     return HttpResponse('yaay')
# @csrf_exempt
# def artiste_list_api(request):
#     if request.method == "GET":
#         songcrud = Artiste.objects.all()
#         serializer = ArtisteSerializer(songcrud, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArtisteSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def artiste_detail_api(request, id):
#     try:
#         artiste = Artiste.objects.get(id=id)
#     except artiste.DoesNotExist:
#         return JsonResponse({"message":"Artiste not found"}, status=404)

#     if request.method == "GET":
#         serializer = ArtisteSerializer(artiste)
#         return JsonResponse(serializer.data, status=200)
#     if request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArtisteSerializer(artiste, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     if request.method == "DELETE":
#         artiste.delete()
#         return JsonResponse({"message":"Artiste deleted"}, status=204)


@csrf_exempt
def song_list_api(request):
    if request.method == "GET":
        songcrud = Song.objects.all()
        serializer = SongSerializer(songcrud, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def song_detail_api(request, id):
    try:
        song = Song.objects.get(id=id)
    except song.DoesNotExist:
        return JsonResponse({"message":"Song not found"}, status=404)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data, status=200)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        song.delete()
        return JsonResponse({"message":"Song deleted"}, status=204)