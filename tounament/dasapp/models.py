from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER ={
        (1,'admin'),
        (2,'doc'),
        
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Specialization(models.Model):
    sname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sname
   
    

class DoctorReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    mobilenumber = models.CharField(max_length=11)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.admin:
            return f"{self.admin.first_name} {self.admin.last_name} - {self.mobilenumber}"
        else:
            return f"User not associated - {self.mobilenumber}"

class PatientReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    mobilenumber = models.CharField(max_length=11,unique=True)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    appointmentnumber = models.IntegerField(default=0)
    spec_id = models.ForeignKey(Specialization, on_delete=models.CASCADE,default=0)
    pat_id = models.ForeignKey(PatientReg, on_delete=models.CASCADE,default=0)    
    date_of_appointment = models.CharField(max_length=250)
    time_of_appointment = models.CharField(max_length=250)
    doctor_id = models.ForeignKey(DoctorReg, on_delete=models.CASCADE)
    additional_msg = models.TextField(blank=True)
    remark = models.CharField(max_length=250,default=0)
    status = models.CharField(default=0,max_length=200)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

class Page(models.Model):
    pagetitle = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    aboutus = models.TextField()
    email = models.EmailField(max_length=200)
    mobilenumber = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pagetitle

class AddPatient(models.Model):
    doctor_id = models.ForeignKey(DoctorReg, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    mobilenumber = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()
    
    medicalhistory = models.TextField()
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MedicalHistory(models.Model):
    pat_id = models.ForeignKey(AddPatient, on_delete=models.CASCADE, related_name='medical_histories', default=0)
    bloodpressure = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)
    bloodsugar = models.CharField(max_length=250)
    bodytemp = models.CharField(max_length=250)
    prescription = models.TextField()
    visitingdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 
