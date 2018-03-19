"""Kindergarten_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from kindergarten_app.views import MainView, AllChildrenView, AddChildView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^main', MainView.as_view()),
    url('^all_children', AllChildrenView.as_view()),
    url('^add_child', AddChildView.as_view(), name="add-child"),
    #url(r'^child/(?P<child_id>(\d)+)', ChildView.as_view(),
       # name="student-group"),

]
