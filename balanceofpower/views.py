from django.shortcuts import render, HttpResponse
from .forms import InfoForm
import pandas as pd
from .algo import input_output
from .scraper2 import scraper2
import time


from django.contrib.staticfiles import finders
# Create your views here.
def index(request):
    #Basic - Doesnt need to be altered
    return render(request, 'index.html')

def formfill(request):
    form = InfoForm()
    return render(request, 'formfill.html',{'form':form})

def latest(request):
    #Basic - Doesnt need to be altered
    return render(request, 'latest.html')

def results(request):
    countries = request.POST.getlist('country_list')
    parameters = request.POST.getlist('parameter_list')
    #print(parameters)
    # Write code for processing the form information. The form information should be passed to appropriate functions for processing and finally call results function for display
    #Write information for displaying of results. All the required data is in the form.
    scraper2()
    df = input_output(countries,parameters,[1 for i in range(len(parameters))])
    table = df.to_html(index = False, classes = 'table')
    return render(request, 'results.html',{'table':table})

#Testing html form objects
def test2(request):
    countries = request.POST.getlist('country_list')
    return HttpResponse(countries)


#Only for static files testing. No use in balance of power application
def test(request):
    result = finders.find('css/agency.css')
    if result==None:
        result = 'None'
    return HttpResponse(result)
