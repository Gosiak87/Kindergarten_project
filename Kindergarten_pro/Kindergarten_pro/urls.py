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
from django.conf.urls import url
from kindergarten_app.views import (
    MainView,
    AllChildrenView, AddChildView, AllTeacherView, AllGroupsView, AddTeacherView, AddGroupView, ShowChildView,
    ShowTeacherView, ShowGroupView, AllTripsView, ShowTripView, AddTripView, UserLoginView,
    UserLogoutView, ModifyChildView, AddPresenceChildView,
    ModifyTripView, ModifyGroupView, ModifyTeacherView, DeleteChildView, DeleteGroupView, DeleteTeacherView,
    DeleteTripView, SendMailView, ShowPresenceView, ShowPaymentView, AllPresencesView )


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^main$', MainView.as_view(), name="main"),
    url(r'^all_children$', AllChildrenView.as_view()),
    url(r'^add_child$', AddChildView.as_view(), name="add-child"),
    url(r'^all_teachers$', AllTeacherView.as_view()),
    url(r'^add_teacher$', AddTeacherView.as_view(), name="add-teacher"),
    url(r'^all_groups$', AllGroupsView.as_view()),
    url(r'^add_group$', AddGroupView.as_view(), name="add-group"),
    url(r'^show_child/(?P<id>(\d)+)$', ShowChildView.as_view(), name="show-child"),
    url(r'^show_teacher/(?P<id>(\d)+)$', ShowTeacherView.as_view(), name="show-teacher"),
    url(r'^show_group/(?P<id>(\d)+)$', ShowGroupView.as_view(), name="show-group"),
    url(r'^all_trips$', AllTripsView.as_view()),
    url(r'^show_trip/(?P<id>(\d)+)$', ShowTripView.as_view(), name="show-trip"),
    url(r'^add_trip$', AddTripView.as_view(), name="add-trip"),
    url(r'^login$', UserLoginView.as_view(), name="login"),
    url(r'^logout$', UserLogoutView.as_view(), name="logout"),
    url(r'^modify_child/(?P<pk>(\d)+)/$', ModifyChildView.as_view(), name="modify-child"),
    url(r'^modify_trip/(?P<pk>(\d)+)/$', ModifyTripView.as_view()),
    url(r'^modify_group/(?P<pk>(\d)+)/$', ModifyGroupView.as_view()),
    url(r'^modify_teacher/(?P<pk>(\d)+)/$', ModifyTeacherView.as_view()),
    url(r'^add_presence_children/(?P<group_id>(\d)+)/$', AddPresenceChildView.as_view()),
    url(r'^delete_child/(?P<pk>(\d)+)/$', DeleteChildView.as_view()),
    url(r'^delete_group/(?P<pk>(\d)+)/$', DeleteGroupView.as_view()),
    url(r'^delete_teacher/(?P<pk>(\d)+)/$', DeleteTeacherView.as_view()),
    url(r'^delete_trip/(?P<pk>(\d)+)/$', DeleteTripView.as_view()),
    url(r'^send_mail/$', SendMailView.as_view(), name='send-mail'),
    url(r'^show_payment/(?P<pk>(\d)+)$', ShowPaymentView.as_view(), name='show-payment'),
    url(r'^show_presence/(?P<pk>(\d)+)/$', ShowPresenceView.as_view(), name="presence"),
    url(r'^all_presence_lists$', AllPresencesView.as_view()),

]
