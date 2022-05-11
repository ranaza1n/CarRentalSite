from django.urls import path
from . import views
urlpatterns = [ path('home', views.index, name='index'),
                path('about', views.about, name='about'),
                path('service', views.services, name='services'),
                path('help', views.help, name='help'),
                path('a', views.a, name='help'),
                path('b', views.b, name='help'),
                path('c', views.c, name='help'),
                path('howitworks', views.howitworks, name='howitworks'),
                path('contact', views.contact, name='contact'),
                path('login', views.login, name='login'),
                path('register', views.register, name='register'),
                path('book',views.book,name = 'book'),
                path('info',views.info,name = 'info'),
                path('history',views.history,name = 'history'),
                path('thank', views.thank, name='thank'),
                path('addcar', views.addcar, name='addcar'),
                path('changeloc', views.changeloc, name='changeloc')]