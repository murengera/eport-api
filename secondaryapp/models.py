from django.db import models
from django.conf import settings
import uuid
from django.contrib.postgres.fields import JSONField,ArrayField



class Category(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return str(self.name)
  

class Secondary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phones = ArrayField(models.CharField(max_length=13))
    emails = ArrayField(models.EmailField(blank=True))
    sector =  models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    ol_fees= models.IntegerField()
    al_fees= models.IntegerField()
    students = models.IntegerField(default=0)
    combinations = models.TextField(blank=True)
    website = models.URLField(max_length=300,null=True,blank=True)
    logo = models.ImageField(upload_to="images/secondary_school_logos/")
    school_motto = models.CharField(max_length=200, default="", blank=True)
    location = JSONField(default=dict)
    """
    location object format
    {
        "longitude": 0.00000,
        "latitude": 0.0000
    }
    """

    level_choices=(
        ('O_LEVEL','O_LEVEL'),
        ('A_LEVEL','A_LEVEL'),
        ('ALL', 'ALL')
    )
    levels = models.CharField(max_length=15, choices=level_choices, default="ALL")

    gender_choices=(
        ('BOYS','BOYS'),
        ('GIRLS','GIRLS'),
        ('ALL','ALL')
    )
    genders = models.CharField(max_length=15, choices=gender_choices, default="ALL")

    type_choices=(
        ('BOARDING','BOARDING'),
        ('DAYSCHOLAR','DAYSCHOLAR'),
        ('BOTH','BOTH')
    )
    types = models.CharField(max_length=10,choices=type_choices)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    headmaster=models.CharField(max_length=20)
    more_information=models.TextField(default="")
    def __str__(self):
        return str(self.name)



"""
group creation nexinstaff can add school,delete school
studentgroup only  view
schoolstaff(view ,get,and updating informattion on his own school)

delete:
-staff
-ordering choose fields

"""
