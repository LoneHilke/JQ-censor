from django.db import models

# Create your models here.
class Censor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fag = models.ManyToManyField('Fag', related_name='item')
    klassetrin = models.ManyToManyField('Klassetrin', related_name='item')
    teacher = models.ManyToManyField('Teacher', related_name='item')

    def __str__(self):
        return self.firstname

class Fag(models.Model):
    fag = models.CharField(max_length=50)

    def __str__(self):
        return self.fag

class Klassetrin(models.Model):
    klasse = models.CharField(max_length=50)

    def __str__(self):
        return self.klasse

class Teacher(models.Model):
    teacher = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher
