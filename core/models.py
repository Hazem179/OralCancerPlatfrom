from django.db import models
from django.contrib.auth.models import User
# Create your models here.

APPOINTMENT_STATES = (
    ('1','Available'),
    ('2','Not Available'),
)
class Specialization(models.Model):
    name = models.CharField(max_length=100,null = True,blank= True)

class Certification(models.Model):
    name = models.CharField(max_length=100,null = True,blank= True)

class Tag(models.Model):
    name = models.CharField(max_length=100,null = True,blank= True)


class Appointment(models.Model):
    date = models.DateField(null = True,blank= True)
    time = models.TimeField(null = True,blank= True)
    state = models.CharField(max_length=100,null = True,blank= True,choices=APPOINTMENT_STATES)


class Doctor(models.Model):
    name = models.CharField(max_length=100,null = True,blank= True)
    title = models.CharField(max_length=100,null = True,blank= True)
    picture = models.ImageField(upload_to='doctors/',null = True,blank= True)
    brief_description = models.TextField(blank=True,null = True)
    sessions_count = models.IntegerField(default=0,null = True,blank= True)
    years_of_experience = models.IntegerField(default=0,null = True,blank= True)
    session_price = models.IntegerField(default=0,null = True,blank= True)
    reviews_count = models.IntegerField(default=0,null = True,blank= True)

class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    def __str__(self):
        return self.doctor.name

class DoctorCertification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    def __str__(self):
        return self.doctor.name
    
class DoctorAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    def __str__(self):
        return self.doctor.name
class Post(models.Model):
    title = models.CharField(max_length=100,null = True,blank= True)
    likes = models.IntegerField(default=0,null = True,blank= True)
    description = models.TextField(blank=True,null = True)
    post = models.TextField(blank=True,null = True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return self.post.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0,null = True,blank= True)
    comment = models.TextField(blank=True,null = True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.post.title


class VideoBlog(models.Model):
    title = models.CharField(max_length=100,null = True,blank= True)
    description = models.TextField(blank=True,null = True)
    thubnail = models.URLField(blank=True,null = True)
    video = models.URLField(blank=True,null = True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100,null = True,blank= True)
    email = models.EmailField(max_length=100,null = True,blank= True)
    subject = models.CharField(max_length=100,null = True,blank= True)
    message = models.TextField(blank=True,null = True)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name