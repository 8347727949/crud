from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    # GENDER_CHOICES = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other'),
    # ]

    pid= models.AutoField(primary_key=True, db_column='pid',unique=True)
    username = models.CharField(max_length=50, unique=True)
    enrollment = models.IntegerField(default='')
    email = models.EmailField(max_length=100,default='')
    password1 = models.CharField(max_length=100,default='')
    password2 = models.CharField(max_length=100,default='')
    # age = models.IntegerField()
    # gender=models.CharField(max_length=5, choices=GENDER_CHOICES)
    # hobbies = models.ManyToManyField('Hobby')
    # def __str__(self):
    #     return self.username
    class meta:
        db_table=('person')


# class Hobby(models.Model):
#     name = models.CharField(max_length=100)
# def __str__(self):
#         return self.name



class subjectdetail(models.Model):
   # rollno=models.IntegerField()
    s_code=models.IntegerField()
    s_name=models.CharField(max_length=100)
   
    sem=models.IntegerField()
  
   
    class meta:
        db_table=('subjectdetail')

class Hotel(models.Model):
    name=models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('Hotel')


class Programmes(models.Model):
    prog_id = models.AutoField(primary_key=True, db_column='prog_id')
    program_code = models.IntegerField()	
    prog_name = models.CharField(max_length=100)
    prog_duration= models.IntegerField()
   # is_active=models.BooleanField()
    created_at=models.DateTimeField(auto_now= True)
    updated_at= models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table=("program_master")

class Semesters(models.Model):
    semester_id = models.AutoField(primary_key=True, db_column='semester_id')
    semester = models.IntegerField()	
    prog_id = models.ForeignKey(Programmes, verbose_name=("semester"), on_delete=models.CASCADE)
   # is_active=models.BooleanField()
    created_at=models.DateTimeField(auto_now= True)
    updated_at= models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table=("semester_master")


class Cource(models.Model):
    course_id = models.AutoField(primary_key=True, db_column='course_id')
#     semester = models.IntegerField()	
    # prog_id = models.ForeignKey(Programmes, verbose_name=("semester"), on_delete=models.CASCADE)
#    # is_active=models.BooleanField()
#     created_at=models.DateTimeField(auto_now= True)
#     updated_at= models.DateTimeField(auto_now_add=True)
    cource_name = models.CharField(max_length=100)
    class Meta:
        db_table=("cource_master")



class Request_provisional(models.Model):
   
    # course_id = models.ForeignKey(Cource, verbose_name=("cource"), on_delete=models.CASCADE)
    pid = models.ForeignKey(Person, on_delete=models.CASCADE,default='1')
    # sem=models.IntegerField()
    # # name=models.CharField(max_length=100)
    # div=models.CharField(max_length=100)
    # enrollment=models.IntegerField(default='1')
    sem_pro=models.IntegerField()
    reason=models.CharField(max_length=500)
    class meta:
        db_table=('Request_provisional')
    def __str__(self):
        return self.reason

class Request_final_result(models.Model):
    course_id = models.ForeignKey(Cource, verbose_name=("cource"), on_delete=models.CASCADE)
    pid = models.ForeignKey(Person, on_delete=models.CASCADE)
    sem=models.IntegerField()
    name=models.CharField(max_length=100)
    # email = models.EmailField(max_length=100,default='')
    div=models.CharField(max_length=100)
    enrollment=models.IntegerField()
    sem_pro1=models.IntegerField(default=1)
   
    class meta:
        db_table=('Request_final_result')




class Request_bonafide(models.Model):
    
    course_id = models.ForeignKey(Cource, verbose_name=("cource"), on_delete=models.CASCADE)
    pid = models.ForeignKey(Person, on_delete=models.CASCADE)
    sem=models.IntegerField()
    name=models.CharField(max_length=100)
    div=models.CharField(max_length=100)
    enrollment=models.IntegerField()
    reason=models.CharField(max_length=500,default='yash')
   
    class meta:
        db_table=('Request_bonafide')





