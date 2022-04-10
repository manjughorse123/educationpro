from django.db import models
from user.models import User
from django.template.defaultfilters import slugify
# Create your models here.
class University(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name
    
    
class MajorProject(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Language(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Degree(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Subject(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Education(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Curriculum(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

    

class Currency(models.Model):

    name = models.CharField(max_length=255)
    Code = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.name   


class TeacherInfo(models.Model):
  
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name='profile_teacher'
    )
    teach_university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,related_name='teacher_university'
    )
    teach_major_project = models.ForeignKey(
        MajorProject,
        on_delete=models.CASCADE,related_name='teacher_major_project'
    )
    teach_degree = models.ForeignKey(
        Degree,
        on_delete=models.CASCADE,related_name='teacher_degree'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    teach_language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,related_name='teacher_language'
    )
    about = models.TextField(null=True, blank=True)
    teaching_experience = models.CharField(max_length=20)
    teaching_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=300)
    teach_licences= models.URLField(null=True, blank=True)
    teach_vedio = models.URLField(null=True, blank=True)
    teach_idcard = models.URLField(null=True, blank=True)
    teach_certificate= models.URLField(null=True, blank=True)


    def __str__(self):
        return self.user.email
    


class TeacherSubject(models.Model):
  
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name='teacher_sub_id'
    )
    teach_education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,related_name='teacher_education'
    )
    teach_curriculum = models.ForeignKey(
        Curriculum,
        on_delete=models.CASCADE,related_name='teacher_curriculum'
    )
    slug = models.SlugField(null=True, blank=True)
    teach_subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,related_name='teacher_prefered_subject'
    )
    session_rate = models.FloatField(default= 0.0)
   
    def __str__(self):
        return self.teach_subject.name+ "," + self.user.first_name
            
    
class SelectField(models.Model):
    Hour_CHOICES =(
        
        ("1", "07:00 AM"),
        ("2", "08:00 AM"),
        ("3", "09:00 AM"),
        ("4", "10:00 AM"),
        ("5", "11:00 AM"),
        ("6", "12:00 PM"),
        ("7", "01:00 PM"),
        ("8", "02:00 PM"),
        ("9", "03:00 PM"),
        ("10", "04:00 PM"),
        ("11", "05:00 PM"),
        ("12", "06:00 PM"),

        
    )
    hour = models.CharField(max_length=10, choices = Hour_CHOICES)
    
    def __str__(self):
        return  str(self.hour)
        
class TeachAvailability(models.Model):
    
    Day_CHOICES =(
        ("0", "SUN"),
        ("1", "MON"),
        ("2", "TUS"),
        ("3", "WED"),
        ("4", "THU"),
        ("5", "FRI"),
        ("6", "SAT"),
        
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name='teach_availability'
    )
    day = models.CharField(max_length=10, choices = Day_CHOICES)
    availability = models.ManyToManyField(SelectField)
    
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.user.email
    

class BilingInformation(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,related_name='card_teacher'
    )
    bank_name = models.CharField(max_length=20, null=True, blank=True)
    iban = models.CharField(max_length=20, null=True, blank=True)
    account_owner_name = models.CharField(max_length=20,null=True, blank=True)
    Account_number = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    currency = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user+self.bank_name
    


