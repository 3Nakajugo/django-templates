from django.urls import path
from .views import index, meetup_details

urlpatterns = [
path(
    'meetups/', index, name= " all-meetups"
),
path(
    'meetups/<slug:meetup_slug>', meetup_details, name='meetup-details'
)
]