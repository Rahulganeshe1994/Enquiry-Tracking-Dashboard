from django.db import models
class Course(models.Model):
    cname=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    details=models.CharField(max_length=30)
    fees=models.IntegerField()
    def __str__(self) -> str:
        return self.cname+" "+str(self.fees)
class Student(models.Model):
    sname=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    mob=models.CharField(max_length=10)
    branch=models.CharField(max_length=5)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    status=models.CharField(max_length=10)
    date=models.DateField(auto_now=False)
    address=models.TextField()
    qualification=models.CharField(max_length=10)
    sem=models.CharField(max_length=10)
    passout=models.IntegerField()
    doe=models.DateField(auto_now=False)
    def __str__(self) -> str:
        return self.sname+" "+self.course.cname+" "+str(self.course.fees)
class Amount(models.Model):
    student=models.OneToOneField(Student,primary_key=True,on_delete=models.CASCADE)
    total_fee=models.IntegerField()
    remaining=models.IntegerField()
    submitamount=models.CharField(max_length=100)
    submitdate=models.CharField(max_length=100)
    nextpaydate=models.DateField(auto_now=False)
    def __str__(self) -> str:
        return self.student.sname+" "+str(self.remaining)