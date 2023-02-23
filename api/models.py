from django.db import models

# Create your models here Company.

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'),('NON IT','NON IT'),('Mobile Phone','Mobile Phone')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.name +'--'+ self.location

# Create your models here Employees.

class Employess(models.Model):
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    about=models.TextField()
    position=models.CharField(max_length=50, choices=(('Manager','manager'),('software develpoer','sd'),('Project Leader','pl')))

    Company=models.ForeignKey(Company,on_delete=models.CASCADE)


  
    