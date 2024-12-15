from django.db import models

class Programme(models.Model):
    name = models.CharField(max_length=255)  # Name of the programme (e.g., Bricks Challenge)
    duration = models.CharField(max_length=100)  # Duration of the programme (e.g., 36 weeks, 5 days)
    
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)  # Name of the group
    programme = models.ForeignKey(Programme, related_name='groups', on_delete=models.CASCADE)  # Link to the Programme
    description = models.TextField(blank=True, null=True)  # Optional description of the group
    
    def __str__(self):
        return self.name
    

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    birth_date = models.DateField()
    school_level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
