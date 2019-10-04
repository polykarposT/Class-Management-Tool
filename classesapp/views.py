from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.utils.timezone import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
# Create your views here.

def index(request):
    return render(request, 'classesapp/index.html')

@login_required
def logout_request(request):
    logout(request)
    return redirect("/")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Invalid username or password")
        else:
            messages.info(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "classesapp/login.html", {"form":form})



class ClassesListView(ListView):
    queryset = models.Classes.objects.annotate(num_students=Count('students')).order_by('name')
    context_object_name = "classes"
    model = models.Classes

class ClassesDetailView(DetailView):
    context_object_name = "class_detail"
    model = models.Classes
    template_name = "classesapp/class_detail.html"

class ClassesCreateView(CreateView):
    fields = ('name', 'day_and_time')
    model = models.Classes

class ClassesUpdateView(UpdateView):
    fields = ('name', 'day_and_time')
    model = models.Classes

class ClassesDeleteView(DeleteView):
    model = models.Classes
    success_url = reverse_lazy("classesapp:classes_list")


#STUDENTS CLASSES VIEW
class StudentsListView(ListView):
    queryset = models.Students.objects.order_by('student_class')
    context_object_name = "students"
    model = models.Students

class StudentsDetailView(DetailView):
    context_object_name = "student_detail"
    model = models.Students
    template_name = "classesapp/student_detail.html"


class StudentsCreateView(CreateView):
    fields = ('name',)
    model = models.Students

    def form_valid(self, form):
        student_class = get_object_or_404(models.Classes,  pk=self.kwargs['pk'])
        form.instance.student_class = student_class
        return super(StudentsCreateView, self).form_valid(form)


class StudentsView(CreateView):
    fields = ('name',)
    model = models.Students


class StudentsUpdateView(UpdateView):
    fields = ('name', 'student_class')
    model = models.Students


class StudentsDeleteView(DeleteView):
    model = models.Students
    success_url = reverse_lazy("classesapp:students_list")


# STATISTICS CLASSES VIEW
class StatisticsCreateView(CreateView):
    fields = ('date', 'dictation_score','writing_score', 'test_score', 'grammar_score', 'in_class_performance')
    model = models.Statistics

    def form_valid(self, form):
        student = get_object_or_404(
            models.Students,  pk=self.kwargs['pk'])
        form.instance.student = student
        return super(StatisticsCreateView, self).form_valid(form)

class StatisticsUpdateView(UpdateView):
    fields = ('student','date', 'dictation_score','writing_score', 'test_score', 'grammar_score', 'in_class_performance')
    model = models.Statistics


class StatisticsDeleteView(DeleteView):
    model = models.Statistics
    success_url = reverse_lazy("classesapp:classes_list")


