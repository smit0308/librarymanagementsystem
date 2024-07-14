"""
URL configuration for librarymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('app1/',include('app1.urls')),
    path('search/', views.search, name='search'),
    path('user/', views.user, name='user'),
    path('books/', views.get_books, name='get_books'),
    path('search_books/', views.search_books, name='search_books'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('get_books/', views.get_books, name='get_books'),
    path('all_books/', views.search_bk, name='all_books'),
    path('add_booked/',views.add_booked,name='add_booked'),

]

