"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# here we are importing 'settings' & 'static'
from django.conf import settings
from django.conf.urls.static import static





'''
Here below we should configure URL Pattern for our "view"

Why we should Configure URL Pattern?---Answer below

NOTICE: This URL can be used by End User to send the request
to our "view" Function by typing "http://localhost:8000/hello1"
'''

urlpatterns = [

    path('', include('account.urls')),

    path('travello', include('travello.urls')),


    path('admin/', admin.site.urls),


    # path('', include('posts.urls')),

    # path('', include('calc_page.urls')),

]



urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



















