from django.urls import path
from .views import index, meetup_detials

urlpatterns = [
path(
    'meetups/', index
),
path(
    'meetups/<slug:meetup_slug>', meetup_detials
)
]