from django.db import models

# Create your models here.
class Censor(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    fag = models.ManyToManyField('Fag', related_name='item')
    klassetrin = models.ManyToManyField('Klassetrin', related_name='klasse')
    teacher = models.ManyToManyField('Teacher', related_name='teacher')

    def __str__(self):
        return self.navn

class Fag(models.Model):
    fag = models.CharField()

    def __str__(self):
        return self.fag

class Klassetrin(models.Model):
    klasse = models.CharField()

    def __str__(self):
        return self.klasse

class Teacher(models.Model):
    teacher = models.CharField()

    def __str__(self):
        return self.teacher
