from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.contrib.auth.models import User






class University(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    email = ArrayField(models.EmailField(max_length=50))
    phone = ArrayField(models.CharField(max_length=12))
    website = models.URLField(max_length=100)
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
   # created_at=models.DateTimeField(null=True, blank=True)
    #key_person=JSONField(default=dict)
    more_info = models.TextField(blank=True)
    log = models.ImageField(upload_to="images/universit_logs/")
    ownershipstatus = [
        ('PUBLIC', 'PUBLIC'),
        ('PRIVATE', 'PRIVATE'),
    ]
    ownershipstatus = models.CharField(
        max_length=10,
        choices=ownershipstatus,
        default='PUBLIC',
    )

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return str((self.name))





class Program(models.Model):

    program = models.CharField(max_length=200, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    duration=models.IntegerField(default=4)
    def __str__(self):
        return str((self.university.name, self.program))


class Facult(models.Model):
    name = models.CharField(max_length=200)


    fees = models.IntegerField(default=0)
    course = ArrayField(models.CharField(max_length=50))
    programoffer = models.ForeignKey(Program, on_delete=models.CASCADE, null= True, blank=True)
    university=models.ForeignKey(University,on_delete=models.CASCADE,null=True,related_name='facults')


    def __str__(self):
        return str((self.name,self.fees))

    def save(self,*args,**kwargs):
        if self.fees<=0:
           raise Exception("invalid fees")
        super(Facult,self).save(*args,**kwargs)


class Department(models.Model):
    name = models.CharField(max_length=200, null=True)
    head_department = models.CharField(max_length=200)
    contacts = models.IntegerField(null=True)
    email = models.EmailField(unique=True, max_length=200)
    facult = models.OneToOneField(Facult, on_delete=models.CASCADE)


    def __str__(self):
        return str((self.name, self.head_department, self.contacts, self.email, self.facult))





