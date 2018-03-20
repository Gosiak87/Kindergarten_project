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
from kindergarten_app.views import (
    MainView,
    AllChildrenView, AddChildView, AllTeacherView, AllGroupsView, AddTeacherView, AddGroupView, ShowChildView, ShowTeacherView, ShowGroupView, AllTripsView, ShowTripView, AddTripView)


urlpatterns = [
    url('admin/', admin.site.urls),
    url('^main', MainView.as_view()),
    url('^all_children', AllChildrenView.as_view()),
    url('^add_child', AddChildView.as_view(), name="add-child"),
    url('^all_teacher', AllTeacherView.as_view()),
    url('^add_teacher', AddTeacherView.as_view(), name="add-teacher"),
    url('^all_group', AllGroupsView.as_view()),
    url('^add_group', AddGroupView.as_view(), name="add-group"),
    url('^show_child/(?P<id>(\d)+)', ShowChildView.as_view(), name="show-child"),
    url('^show_teacher/(?P<id>(\d)+)', ShowTeacherView.as_view(), name="show-teacher"),
    url('^show_group/(?P<id>(\d)+)', ShowGroupView.as_view(), name="show-group"),
    url('^all_trips', AllTripsView.as_view()),
    url('^show_trip/(?P<id>(\d)+)', ShowTripView.as_view(), name="show-trip"),
    url('^add_trip', AddTripView.as_view(), name="add-trip"),

    #url(r'^child/(?P<child_id>(\d)+)', ChildView.as_view(),
       # name="student-group"),

]
