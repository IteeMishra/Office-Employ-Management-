from django.db import models

# Create your models here.
class Role(models.Model):
    name=models.CharField(max_length=200,null=False)
        #with help of this function this model's objects will appear using these values and not as object1 ,object2 
    def __str__(self) :
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(Department, on_delete = models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    phone=models.IntegerField(null=False)
    hire_date=models.DateField()
    def __str__(self):
        return self.first_name
    