from django.urls import path

from room import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.store, name='store'),
    path('gallery/create', views.storeGallery, name='storeGallery'),
    path('<int:room_id>',views.room_details, name='room_details'),
]
