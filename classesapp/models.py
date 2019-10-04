from django.db import models
from django.urls import reverse
# Create your models here.

class Classes(models.Model):
    name = models.CharField(max_length=256)
    day_and_time= models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classesapp:class_detail", kwargs={"pk": self.pk})


class Students(models.Model):
    name = models.CharField(max_length=256)
    student_class =  models.ForeignKey(
        Classes, related_name = 'students', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classesapp:student_detail", kwargs={"pk": self.pk})

class Statistics(models.Model):
    student= models.ForeignKey(
        Students, related_name='statistics', on_delete=models.CASCADE, null=True
    )
    date = models.DateField(blank=True, null=True)
    dictation_score = models.FloatField()
    writing_score = models.FloatField()
    test_score = models.FloatField()
    grammar_score = models.FloatField()
    in_class_performance = models.FloatField()
    
    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse("classesapp:students_list")
    
