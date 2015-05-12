from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    #the render function is made to take a parameter from the template folder.
    #this is why the location of the template folder is important.
    return render(request, 'rango/index.html', context_dict)
def about(request):
    return HttpResponse("Rango says here is the about page. <br/><a href = /rango>Index</a>")
