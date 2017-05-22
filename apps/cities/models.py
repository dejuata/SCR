from django.db import models


class DepartmentColombia(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        ordering = ['name']


class CitiesColombia(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(DepartmentColombia, related_name="cities", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
