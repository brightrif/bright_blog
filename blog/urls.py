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

from django.urls import path, include
from .views import homeview, blogPostDetailView, post_create_view, post_update ,myposts

urlpatterns = [
    path('', homeview, name='bloghome'),
    path('<str:slug>/', blogPostDetailView, name='blogdetail'),
    path('addpost',post_create_view,name='post_create'),
    path('<str:slug>/update/', post_update, name='post_update'),
    path('myposts', myposts, name='myposts' )
]
