"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib  import admin
from django.urls import path
from myapp import views
admin.site.site_header = "RPD.COM admin"
admin.site.site_title = "RPD.com Admin Portal"
admin.site.index_title = "Welcome to RPD.com Researcher Portal"
urlpatterns = [
path('admin/', admin.site.urls),
path('home',views.index,name='home'),
path('',views.index,name='home'),
path('about',views.about,name='about'),
path('blog',views.blog,name='services'),
path('business',views.business,name='business'),
path('contact',views.contact,name='contact'),
path('covid-19-donation',views.covid_19_donation,name='covid-19-donation'),
path('blog/how-to-fight-covid',views.how_to_fight_covid,name='how_to_fight_covid')
]
