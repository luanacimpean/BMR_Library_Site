from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

from .models import Series, Subseries


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('archive/index.html')
    #context = {
        #'latest_question_list': latest_question_list,
    #}

    series_list = Series.objects.order_by('-series_number')
    template = loader.get_template('archive/index.html')
    context = {
        'series_list': series_list,
    }    
    
    return render(request, 'archive/index.html', context)   