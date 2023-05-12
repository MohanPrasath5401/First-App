
from django.db import models

# Create your models here.
class Student(models.Model): #firstApp will be mysql
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stumail = models.EmailField(max_length=100)
    stuclass = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.stuid)

class MasterData(models.Model): 
    class Meta:
       unique_together = (('stuid','subject'),)
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stumail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.stuid)

class Mark_attendance(models.Model):
    class Meta:
            unique_together = (('uid','date1'),("date1","ip_address"))
    uid = models.ForeignKey("MasterData",related_name ="uid",on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    time1 = models.IntegerField(null=False)
    ip_address = models.EmailField(max_length=100,null=False)
    date1 = models.CharField(max_length=100,null=False)
    platform = models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return str(self.uid)
