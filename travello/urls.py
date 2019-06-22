from django.urls import path
from . import views


app_name="travello"


'''
Here below we should configure URL Pattern for our "view"
'''

urlpatterns = [


    path('', views.index, name='index'),

    #path('', views.homepage, name="homepage")


]



