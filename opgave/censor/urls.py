from django.urls import path
from .views import Index, Alle

urlpatterns = [
    path('',  Index.as_view(), name='index'),
    path('alle/', Alle.as_view(), name='alle'),
]