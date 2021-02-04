"""bright URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import login_view, register_view, logout_view, dashboard_view, userupdate_view, user_info, add_messages

app_name = "account"

urlpatterns = [
    # path('', ),
    path('login/', login_view, name="login"),  
    path('register/', register_view, name="register"), 
    path('logout/', logout_view, name="logout"),
    path('dashboard',dashboard_view, name = "dashboard"),
    path('userupdate/<int:pk>',userupdate_view, name ="userupdate"),
    path("user_info/", user_info),
    path("add_messages/", add_messages),
]

