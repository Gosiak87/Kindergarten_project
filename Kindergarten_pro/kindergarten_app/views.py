import datetime

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import UpdateView, CreateView

from kindergarten_app.models import PresenceList
from .models import Child, Teacher, Group, Carer, Trip
from .forms import ChildAddForm, CarerAddForm, TeacherAddForm, GroupAddForm, TripAddForm, LoginForm
from django.urls import reverse


# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, template_name="main.html")


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            "form": form
        }
        return render(request, template_name="user_login.html", context=ctx)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Udało się zalogować")
            return HttpResponse("No nie koniecznie")


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('index'))


class AllChildrenView(View):
    def get(self, request):
        children = Child.objects.all()

        ctx = {
            "children": children,
        }

        return render(request,
                      template_name="all_children.html",
                      context=ctx)


class ShowChildView(View):
    def get(self, request, id):
        child = Child.objects.get(id=id)
        #carer = Carer.objects.get(id=id)

        ctx = {
            "child": child,
            #"carer": carer,
        }
        return render(request,
                      template_name="show_child.html",
                      context=ctx)


class DeleteChildView(View):
    def get(self, request, id):
        child = Child.objects.get(id=id)
        child.delete()
        return HttpResponse("Przedszkolak został usunięty")


class AddChildView(View):
    def get(self, request):
        form = ChildAddForm()
        carer_1_form = CarerAddForm(prefix='carrer-1')
        carer_2_form = CarerAddForm(prefix='carrer-2')

        ctx = {
            "form": form,
            "carer_1_form": carer_1_form,
            "carer_2_form": carer_2_form
        }
        return render(request,
                      template_name="add_child.html",
                      context=ctx)

    def post(self, request):
        form = ChildAddForm(request.POST)
        carer_1_form = CarerAddForm(request.POST, prefix="carrer-1")
        carer_2_form = CarerAddForm(request.POST, prefix="carrer-2")

        if form.is_valid() and carer_1_form.is_valid() and carer_2_form.is_valid():
            child = form.save()

            carer_1 = carer_1_form.save()
            carer_2 = carer_2_form.save()

            child.carers.add(carer_1)
            child.carers.add(carer_2)

            return redirect(reverse('show-child', kwargs={'id': child.id}))
        ctx = {
            'form': form,
            'carer_1_form': carer_1_form,
            'carer_2_form': carer_2_form,
        }
        return render(request,
                      template_name="add_child.html",
                      context=ctx)


class AllTeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()

        ctx = {

            "teachers": teachers,
        }

        return render(request,
                      template_name="all_teachers.html",
                      context=ctx)


class ShowTeacherView(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)

        ctx = {
            "teacher": teacher,

        }
        return render(request,
                      template_name="show_teacher.html",
                      context=ctx)


class AddTeacherView(View):
    def get(self, request):
        form = TeacherAddForm()
        ctx = {
            "form": form,
        }
        return render(request,
                      template_name="add_teacher.html",
                      context=ctx)

    def post(self, request):
        form = TeacherAddForm(request.POST)

        if form.is_valid():
            teacher = form.save()

            return redirect(reverse('show-teacher', kwargs={'id': teacher.id}))
        ctx = {
            'form': form,
        }
        return render(request,
                      template_name="add_teacher.html",
                      context=ctx)


class AllGroupsView(View):
    def get(self, request):
        groups = Group.objects.all()
        ctx = {
            "groups": groups,
        }
        return render(request,
                      template_name="all_groups.html",
                      context=ctx)


class ShowGroupView(View):
    def get(self, request, id):
        group = Group.objects.get(id=id)

        ctx = {
            "group": group,

        }
        return render(request,
                      template_name="show_group.html",
                      context=ctx)


class AddGroupView(View):
    def get(self, request):
        form = GroupAddForm()
        ctx ={
            "form": form,
        }
        return render(request, template_name="add_group.html",
                      context=ctx)

    def post(self, request):
        form = GroupAddForm(request.POST)

        if form.is_valid():
            group = form.save()

            return redirect(reverse("show-group", kwargs={"id": group.id}))
        ctx = {
            "form": form,
        }
        return render(request,
                      template_name="add_group.html",
                      context=ctx)


class AllTripsView(View):
    def get(self, request):
        trips = Trip.objects.all()

        ctx = {

            "trips": trips,
        }

        return render(request,
                      template_name="all_trips.html",
                      context=ctx)


class ShowTripView(View):
    def get(self, request, id):
        trip = Trip.objects.get(id=id)

        ctx = {
            "trip": trip,

        }
        return render(request,
                      template_name="show_trip.html",
                      context=ctx)


class AddTripView(View):
    def get(self, request):
        form = TripAddForm()
        ctx = {
            "form": form,
        }
        return render(request,
                      template_name="add_trip.html",
                      context=ctx)

    def post(self, request):
        form = TripAddForm(request.POST)

        if form.is_valid():
            trip = form.save()

            return redirect(reverse("show-trip", kwargs={"id": trip.id}))
        ctx = {
            "form": form,
        }
        return render(request,
                      template_name="add_trip.html",
                      context=ctx)


class PresenceChildrenView(View):
    def get(self, request):
        form = PresenceListForm()
        ctx ={
            "form": form,
        }
        return render(request,
                      template_name="presence_children.html",
                      context=ctx)


class AddPresenceChildView(CreateView):
    template_name = "add_presence.html"
    model = PresenceList
    success_url = "/"

    fields = ['children']

    def dispatch(self, request, *args, **kwargs):
        self.group_id = kwargs.pop('group_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        presence_list = form.save(commit=False)

        group = Group.objects.get(pk=self.group_id)
        presence_list.group = group
        presence_list.day = datetime.date.today()
        presence_list.save()

        form.save_m2m()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return '/show_group/{}'.format(self.group_id)


class ShowPresenceListView(CreateView):
    template_name = "show_presence.html"
    model = PresenceList


class ModifyChildView(UpdateView):
    template_name = "modify_child.html"
    model = Child
    success_url = "/"
    fields = '__all__'

    # def dispatch(self, request, *args, **kwargs):
    #     self.child_id = kwargs.pop('child_id')
    #     return super().dispatch(request, *args, **kwargs)
    # #
    # def form_valid(self, form):
    #     modify_child = form.save(commit=False)
    #
    #     modify_child = Child.objects.get(pk=self.child_id)
    #     child.first_name = first_name
    #     presence_list.day = datetime.date.today()
    #     presence_list.save()
    #
    #     form.save_m2m()
    #     return redirect(self.get_success_url())

    # def get_success_url(self):
    #     return '/show_child/{}'.format(self.child_id)

    #redirect(reverse("show-child", kwargs={"id": child.id}))


class ModifyTeacherView(UpdateView):
    template_name = "modify_teacher.html"
    model = Teacher
    success_url = "/"
    fields = '__all__'


class ModifyTripView(UpdateView):
    template_name = "modify_trip.html"
    model = Trip
    success_url = "/"
    fields = '__all__'


class ModifyGroupView(UpdateView):
    template_name = "modify_group.html"
    model = Group
    success_url = "/"
    fields = '__all__'
    # def post(self, request, id):
    #     child = Child.objects.get(id=id)
    #
    #     return redirect(reverse("show-child", kwargs={"id": child.id}))
    #
    #

