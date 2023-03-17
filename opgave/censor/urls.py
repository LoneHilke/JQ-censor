from django.urls import path
from .views import Index, Alle, Fag, Dansk, Tysk, Engelsk, Matematik, Klassetrin, Klasse9, Klasse10

urlpatterns = [
    path('',  Index.as_view(), name='index'),
    path('alle/', Alle.as_view(), name='alle'),
    path('fag/', Fag.as_view(), name='fag'),
    path('dansk/', Dansk.as_view(), name='dansk'),
    path('tysk/', Tysk.as_view(), name='tysk'),
    path('engelsk/', Engelsk.as_view(), name='engelsk'),
    path('matematik/', Matematik.as_view(), name='matematik'),
    path('klassetrin/', Klassetrin.as_view(), name='klassetrin'),
    path('9klasse/', Klasse9.as_view(), name='9klasse'),
    path('10klasse/', Klasse10.as_view(), name='10klasse'),
]