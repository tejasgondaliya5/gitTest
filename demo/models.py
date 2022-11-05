from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField

# Create your models here.
spacialist = [
    ('select','select'),
    ('Dentist','Dentist'),
    ('Homeyopethic','Homeyopethic'),
    ('Orthopedic','Orthopedic'),
]
class Addnurse(models.Model):
    Nurse_name = models.CharField(default='', max_length=50)
    Nurse_specialist = models.CharField(default='', choices=spacialist, max_length=20)
    Nurse_email = models.EmailField(default='', max_length=100)
    Nurse_number = models.PositiveBigIntegerField(default='+91')
    Nurse_expirence = models.CharField(default='', max_length=25)
    Nurse_fees = models.CharField(default='', max_length=20)
    Nurse_password = models.CharField(default='', max_length=12)

    def __str__(self):
        return self.Nurse_name

class UserDetail(models.Model):
    Name = models.CharField(default='', max_length=50)
    Email = models.EmailField(default='', max_length=100)
    Number = models.PositiveBigIntegerField(default='+91')
    Password = models.CharField(default='', max_length=12)
    Confirm_password = models.CharField(default='', max_length=12)

    def __str__(self):
        return self.Name

spacialist2 = [
    ('select','select'),
    ('Dentist','Dentist'),
    ('Homeyopethic','Homeyopethic'),
    ('Orthopedic','Orthopedic'),
]
class Cart(models.Model):
    joinuser = models.ForeignKey('UserDetail', default='', on_delete=models.CASCADE)
    joinNurse=models.ForeignKey('Addnurse',default='',on_delete=models.CASCADE)
    joinshedule=models.ForeignKey('Setshedule',default='',on_delete=models.CASCADE)
    Message = models.CharField(default='', max_length=1000)
    Trigger=models.IntegerField(default=0)


    def __str__(self):
        return self.joinuser.Name
        
root=[
    ('select','select'),
    ('Morning','Morning'),
    ('Afternoot','Afternoot'),
    ('Evning','Evning')
]
class Setshedule(models.Model):
    join_N = models.ForeignKey('Addnurse',default='',on_delete=CASCADE)
    Date = models.DateField()
    Root = models.CharField(default='', choices=root, max_length=20)
    Start_time = models.TimeField(auto_now_add=False)
    End_time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return self.join_N.Nurse_name



        