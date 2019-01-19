from . import id_checker

try:
    check(request)
except:
   return(HttpResponse('<h1> It failed for some reason... </h1>'))