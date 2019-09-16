from django.shortcuts import render
from django.http import HttpResponse


from .models import ID
from .lib.check import check,make,basic
from .lib.dumps import time_check
# Create your views here.

def id_check(request):

    #Scripts
    a = check(request)

    #Main

    all_data = ID.objects.all()
    context = {
        'all_data' : all_data,
    }
    if a == True:
        return(render(request, 'index/index.html', context ))
    else:
        return(HttpResponse("<h1> Let's get this bread </h1>"))


def dumps(request):
    time_check()

    HttpResponse("<h1> Dump day initiated! </h1>")


def basic_data(request):
    if request.method == "POST":
        a = make(request)
      #  basic(request,a)
        if basic(request,a) == True:
            return(HttpResponse(a))
        else:
            return(HttpResponse('<h1> Nice try <3 </h1>'))
    else:
        return(HttpResponse("<h1>U ain't getting this!</h1>"))    
