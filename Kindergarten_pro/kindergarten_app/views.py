from django.shortcuts import render, redirect
from django.views import View
from .models import Child
from .forms import ChildAddForm
from django.urls import reverse


# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, template_name="main.html")


class AllChildrenView(View):
    def get(self, request): # kindergarten_groups):
        children = Child.objects.all()

        # if children.second_name is None:
        #     children.second_name = ""

        ctx = {
            #"kindergarten_groups": KINDERGARTEN_GROUPS,
            "children": children,
        }

        return render(request,
                      template_name="all_children.html",
                      context=ctx)


class AddChildView(View):
    def get(self, request):
        form = ChildAddForm()
        ctx = {
            "form": form,
        }
        return render(request,
                      template_name="add_child.html",
                      context=ctx)

    def post(self, request):
        form = ChildAddForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            second_name = form.cleaned_data["second_name"]
            last_name = form.cleaned_data["last_name"]
            year_of_birth = form.cleaned_data['year_of_birth']
            group = form.cleaned_data["group"]
            child = Child.objects.create(
                first_name=first_name,
                second_name=second_name,
                last_name=last_name,
                year_of_birth=year_of_birth,
                group=group,
               )
            return redirect(reverse('child-group', args=[child.id]))
        ctx = {
            'form': form
        }
        return render(request,
                      template_name="add_child.html",
                      context=ctx)



