# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name=   models.CharField(max_length=30)
    age=    models.IntegerField()
    high=   models.IntegerField()

class Author(models.Model):
    name=   models.CharField(max_length=50)
    email = models.EmailField()

class Entry(models.Model):
    person=     models.ForeignKey(Person)
    headline =  models.CharField(max_length=30)
    body_text = models.TextField()
    pub_date =  models.DateField()
    mod_date =  models.DateField()
    authors =   models.ManyToManyField(Author)
    n_comments =models.IntegerField()
    n_pinbacks =models.IntegerField()
    rating =    models.IntegerField()