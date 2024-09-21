from django.urls import path

from skilltest import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.store, name='store'),
    path('submit', views.submit_test, name='submit_test'),
]

