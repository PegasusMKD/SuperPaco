from django.http import HttpResponse

from .main_funcs import *
import json

def update_choices(request):
    return HttpResponse(json.dumps(update_choice_fields(request)))

def create_user(request):
    return HttpResponse(json.dumps(create_users(request)))
