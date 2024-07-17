"""
URL configuration for libs_portal project.

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
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('home/', views.home, name='home'),
    path('readers/', views.readers_tab, name='readers'),
    path('books/', views.books, name='books'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('returns/', views.returns, name='returns'),
    path('shop/', views.shop, name='shop'),
    path('save/', views.save_student, name='save_student'),
    # Other paths
]
