from django.urls import path
from . import views


app_name="account"


'''
Here below we should configure URL Pattern for our "view"
'''

urlpatterns = [


    path('register', views.register, name='register'),

    #path('', views.homepage, name="homepage")


]



