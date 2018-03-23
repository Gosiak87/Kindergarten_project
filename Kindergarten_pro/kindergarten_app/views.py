import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from kindergarten_app.models import PresenceList
from .models import Child, Teacher, Group, Carer, Trip
from .forms import ChildAddForm, CarerAddForm, TeacherAddForm, GroupAddForm, TripAddForm, LoginForm, PresenceListForm
from django.urls import reverse, reverse_lazy


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

    def post(self, request):
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            return redirect(reverse('main'))
        return render(request, template_name="user_login.html",
                      context={'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("main"))


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


class DeleteChildView(DeleteView):
    model = Child
    template_name = "delete.html"
    success_url = '/'
    #fields = '__all__'

    def get_success_url(self):
         return "/all_children"


class DeleteGroupView(DeleteView):
    model = Group
    template_name = "delete.html"
    success_url = '/'
    fields = '__all__'

    def get_success_url(self):
        return "/all_groups"


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = "delete.html"
    success_url = '/'
    fields = '__all__'

    def get_success_url(self):
        return "/all_teachers"


class DeleteTripView(DeleteView):
    model = Trip
    template_name = "delete.html"
    success_url = '/'
    fields = '__all__'

    def get_success_url(self):
        return "/all_trips"


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


class AddPresenceChildView(CreateView):
    template_name = "add_presence.html"
    model = PresenceList
    form_class = PresenceListForm
    success_url = "/"

    # ustawiamy domyslne wartosci
    # def get_initial(self):
    #     group_pk = self.kwargs.get('group_id')
    #     children = Group.objects.get(id=group_pk).child_set.all()
    #     return {
    #         'children': children,
    #     }

    def get_form(self, form_class=None):
        group_pk = self.kwargs.get('group_id')
        children = Group.objects.get(id=group_pk).child_set.all()
        form = super().get_form(form_class)
        form.fields["children"].queryset = children
        return form

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
        return '/all_presences_lists'


class ShowPresenceView(DetailView):
    template_name = "show_presence.html"
    model = PresenceList
    modelform = PresenceListForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        presence_lists = self.object.group.presencelist_set.exclude(id=self.object.id).order_by('day')
        all_children = self.object.group.child_set.all()
        present_children = self.object.children.all()

        for child in all_children:
            if child in present_children:
                child.present = True

        context.update({
            'presence_list': all_children,
            'presence_lists': presence_lists})
        return context


class AllPresencesView(View):
    def get(self, request):
        presence_lists = PresenceList.objects.all()

        ctx = {

            "presence_lists":  presence_lists,
        }

        return render(request,
                      template_name="all_presences_list.html",
                      context=ctx)


class ModifyChildView(UpdateView):
    template_name = "modify_child.html"
    model = Child
    fields = '__all__'

    def get_success_url(self):
         return "/show_child/{}".format(self.object.pk)

    #redirect(reverse("show-child", kwargs={"id": child.id}))


class ModifyTeacherView(UpdateView):
    template_name = "modify_teacher.html"
    model = Teacher
    success_url = "/"
    fields = '__all__'

    def get_success_url(self):
         return "/show_teacher/{}".format(self.object.pk)


class ModifyTripView(UpdateView):
    template_name = "modify_trip.html"
    model = Trip
    success_url = "/"
    fields = '__all__'

    def get_success_url(self):
         return "/show_trip/{}".format(self.object.pk)


class ModifyGroupView(UpdateView):
    template_name = "modify_group.html"
    model = Group
    success_url = "/"
    fields = '__all__'

    def get_success_url(self):
         return "/show_group/{}".format(self.object.pk)


class SendMailView(View):
    def get(self, request):
        send_mail(
            'Płatność za czesne',
            'Prosimy opłacić do 10 marca',
            'prrzedszkolecl@onet.pl',
            ['prrzedszkolecl@onet.pl'],
            fail_silently=False,
        )
        return HttpResponse('Wyslalem')


class ShowPaymentView(DetailView):
    template_name = "show_payment.html"
    model = Child

    def get_context_data(self, **kwargs):
        context = super(ShowPaymentView, self).get_context_data()

        # dziecko w grupie wyciagnij grupe dziecka
        group = self.object.group
        # listy to
        presence_lists = group.presencelist_set.all()

        counter = 0

        for presence_list in presence_lists:
            if self.object in presence_list.children.all():
                counter += 1

        base_payment = 15000
        day_payment = 100

        payment = base_payment - counter * day_payment

        context.update({
            'presence_lists': presence_lists,
            'payment': payment

        })
        return context
