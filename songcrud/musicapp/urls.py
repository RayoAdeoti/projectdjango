# from django.contrib import admin
from django.urls import path

# from .views import artiste_list_api, artiste_detail_api
from .views import song_list_api, song_detail_api
from . import views
urlpatterns = [
    # path("", views.index, name = "index"),
    # path("songcrud/", artiste_list_api, name="artiste_list_api"),
    # path("songcrud/<int:id>/", artiste_detail_api, name="artiste_detail_api"),
    path("songcrud/", song_list_api, name="song_list_api"),
    path("songcrud/<int:id>/", song_detail_api, name="song_detail_api")
]
