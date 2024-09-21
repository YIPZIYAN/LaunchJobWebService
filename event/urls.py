from django.urls import path

from event import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.store, name='store'),
    path('attendee', views.attendee, name='attendee'),
    path('apply', views.apply, name='apply'),
    path('event-attendee', views.event_attendee, name='event_attendee'),
]