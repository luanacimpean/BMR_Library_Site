from django.db import models
import datetime
import os

from django.utils import timezone
from datetime import datetime

#class Question(models.Model):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

class Series(models.Model):
    series_number = models.CharField(max_length=3)
    subseries_number = models.CharField(max_length=3, default='')
    box_number =  models.CharField(max_length=10, default='') 
    file_number =  models.CharField(max_length=10, default='') 
    pub_date = models.DateTimeField('date published', default=datetime.now)
    publication_series = models.CharField(max_length=100, default='') 
    document_number = models.CharField(max_length=3, default='', blank=True)
    title = models.CharField(max_length=500, default='')
    scanned = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    followup = models.BooleanField(default=False)
    subject = models.CharField(max_length=50, default='', blank=True)
    keywords = models.CharField(max_length=500, default='', blank=True)
    summary = models.CharField(max_length=1000, default='', blank=True)
    research_notes = models.CharField(max_length=1000, default='', blank=True)
    personnel = models.CharField(max_length=1000, default='', blank=True)
    
    def __str__(self):
        return self.series_number    

class Subseries(models.Model):
    subseries_number = models.CharField(max_length=3)
    
    def __str__(self):
        return self.subseries_number      

