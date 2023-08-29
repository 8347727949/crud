from django.db import models

# Create your models here.


class projectdetail(models.Model):
   # rollno=models.IntegerField()
    s_name=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)
    collage=models.CharField(max_length=100)
    enrollment=models.IntegerField()
    sem=models.IntegerField()
    p_year=models.IntegerField()
   
    class meta:
        db_table=('projectdetail')