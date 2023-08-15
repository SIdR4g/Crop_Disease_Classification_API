from django.urls import path
from .views import *

urlpatterns = [
   path('', ActionAPI.as_view()),
   path('view/', ViewAPI.as_view()),
   path('users/', UserActionAPI.as_view()),
]