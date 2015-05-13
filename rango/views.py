from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    #the render function is made to take a parameter from the template folder.
    #this is why the location of the template folder is important.
    return render(request, 'rango/index.html', context_dict)
def about(request):
    context_dict = {'message': "This is rango's cousin. can't you see the resemblance ?"}
    return render(request, 'rango/about.html', context_dict)
