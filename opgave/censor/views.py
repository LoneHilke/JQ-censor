from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Censor, Klassetrin, Fag, Teacher

# Create your views here.
class Index(TemplateView):

    template_name = 'censor/index.html'

class Alle(View):
    def get(self, request, *args, **kwargs):
        fag = Censor.objects.filter(fag__fag__contains ='Fag')
        klassetrin = Censor.objects.all= 'Klassetrin'
        teacher = Censor.objects.all = 'Teacher'

        context= {
            'fag': fag,
            'klassetrin': klassetrin,
            'teacher': teacher
        }
        return render(request, 'censor/alle.html', context)

class Fag(View):
    def get(self, request, *args, **kwargs):
        fag = Censor.objects.filter(fag__fag__contains ='Fag')
        dansk = Censor.objects.filter(fag__fag__contains='dansk')
        tysk = Censor.objects.filter(fag__fag__contains='tysk')
        engelsk = Censor.objects.filter(fag__fag__contains='engelsk')
        matematik = Censor.objects.filter(fag__fag__contains='matematik')

        context= {
            'fag': fag,
            'dansk': dansk,
            'tysk': tysk,
            'matematik': matematik,
            'engelsk': engelsk
        }
        return render(request, 'censor/fag.html', context)
    
class Dansk(View):
    def get(self, request, *args, **kwargs):
        dansk = Censor.objects.filter(fag__fag__contains='dansk')
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'dansk': dansk,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/dansk.html', context)

class Tysk(View):
    def get(self, request, *args, **kwargs):
        tysk = Censor.objects.filter(fag__fag__contains='tysk')
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'tysk': tysk,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/tysk.html', context)
    
class Engelsk(View):
    def get(self, request, *args, **kwargs):
        engelsk = Censor.objects.filter(fag__fag__contains='engelsk')
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'engelsk': engelsk,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/engelsk.html', context)
    
class Matematik(View):
    def get(self, request, *args, **kwargs):
        matematik = Censor.objects.filter(fag__fag__contains='matematik')
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'matematik': matematik,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/matematik.html', context)
    
class Klassetrin(View):
    def get(self, request, *args, **kwargs):
        klassetrin = Censor.objects.all='klassetrin'
        klasse9 = Censor.objects.all='klasse9'
        klasse10 = Censor.objects.all='klasse10'

        context= {
            'klassetrin': klassetrin,
            'klasse9': klasse9,
           'klasse10': klasse10,
        }
        return render(request, 'censor/klassetrin.html', context)

class Klasse9(View):
    def get(self, request, *args, **kwargs):
        klasse9 = Censor.objects.all='klasse9'
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'klasse9': klasse9,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/9klasse.html', context)
    
class Klasse10(View):
    def get(self, request, *args, **kwargs):
        klasse10 = Censor.objects.all='klasse10'
        #klassetrin = Censor.objects.filter( klassetrin__klasse__contains = 'Klassetrin')
        #teacher = Censor.objects.filter(teacher__teacher__contains = 'Teacher')

        context= {
            'klasse10': klasse10,
            #'klassetrin': klassetrin,
            #'teacher': teacher
        }
        return render(request, 'censor/10klasse.html', context)
