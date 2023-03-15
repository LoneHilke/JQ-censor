from django.contrib import admin
from .models import Censor, Fag, Klassetrin, Teacher

# Register your models here.
admin.site.register(Censor)
admin.site.register(Fag)
admin.site.register(Klassetrin)
admin.site.register(Teacher)