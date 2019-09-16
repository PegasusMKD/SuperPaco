from django.contrib import admin
from django.urls import path,include
from ..maindb.main_funcs import *

from threading import Thread

urlpatterns = [
    path('feed/', include('updates.urls')),
    path('back_end/', include('maindb.urls')),
    path('admin/', admin.site.urls),
]

"""
Crane jobs
"""

functions = [dump_timer,back_up_timer]
for func in functions:
    thread = Thread(target = func,setDaemon=True)
    thread.start()

