from django.db import models

# Create your models here.



class Customer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    phone_number=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Helper(models.Model):
    name=models.CharField(max_length=100)
    gender_options=(('Male','Male'),('Female','Female'),('Trans','Trans'))
    gender=models.CharField(max_length=100,choices=gender_options)
    skills=models.CharField(max_length=200)
    age=models.IntegerField()
    customer=models.OneToOneField(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    
