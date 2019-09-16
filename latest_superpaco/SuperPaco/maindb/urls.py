from django.urls import path,include
from . import views

urlpatterns = [
    #Checking ID, and if non-existent, makes one (/back-end/id-check/)
    path('id_check/', views.update_choices, name = 'update_choices'),
    #Basic user data(age, gender, q1, q2)
    path('basic_data/', views.create_user, name="create_user"),
]
