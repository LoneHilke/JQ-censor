from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Censor, Klassetrin, Fag, Teacher

# Create your views here.
class Index(TemplateView):

    template_name = 'censor/base.html'

class Alle(View):
    def get(self, request, *args, **kwargs):
        fag = Censor.objects.all ='Fag'
        klassetrin = Censor.objects.all = 'Klassetrin'
        teacher = Censor.objects.all = 'Teacher'

        context= {
            'fag': fag,
            'klassetrin': klassetrin,
            'teacher': teacher
        }
        return render(request, 'censor/alle.html', context)

