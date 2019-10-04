from django.urls import path
from classesapp import views

app_name = 'classesapp'

urlpatterns = [
    path('', views.ClassesListView.as_view(), name="classes_list"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('class/<int:pk>/', views.ClassesDetailView.as_view(), name="class_detail"),
    path('new/', views.ClassesCreateView.as_view(), name="classes_create"),
    path('class/<int:pk>/update/', views.ClassesUpdateView.as_view(), name="classes_update"),
    path('class/<int:pk>/delete/', views.ClassesDeleteView.as_view(), name="classes_delete"),
    path('class/<int:pk>/student/new/', views.StudentsCreateView.as_view(), name="student_create"),
    path('students/', views.StudentsListView.as_view(), name="students_list"),
    path('student/<int:pk>/', views.StudentsDetailView.as_view(), name="student_detail"),
    path('student/<int:pk>/update/', views.StudentsUpdateView.as_view(), name="student_update"),
    path('student/<int:pk>/delete/', views.StudentsDeleteView.as_view(), name="student_delete"),
    path('student/<int:pk>/statistics/new/', views.StatisticsCreateView.as_view(), name="statistics_create"),
    path('statistic/<int:pk>/update/', views.StatisticsUpdateView.as_view(), name="statistic_update"),
    path('statistic/<int:pk>/delete/', views.StatisticsDeleteView.as_view(), name="statistic_delete"),
]
