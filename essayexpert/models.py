from django.db import models
from django.utils import timezone
import datetime
from accounts.models import Profile
from django.utils.text import slugify

class Discipline(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    

class SubDiscipline(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name="sub_discipline")
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class PaperType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"


class PowerPoint(models.Model):
    count = models.PositiveIntegerField(default=0, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=3.00, editable=False)
    
    def __str__(self):
        return str(self.count)
    
    @property
    def get_amount(self):
        return f"{(self.count*self.price):2f}"
    
    def save(self, *args, **kwargs):
        self.price = float(self.get_amount)
        return super(PowerPoint, self).save(*args, **kwargs)
    


PAPER_TYPE_CHOICES = [(paper_type.name, paper_type.name) for paper_type in PaperType.objects.all()]
DISCIPLINE_CHOICES = [(discipline.name, discipline.name) for discipline in Discipline.objects.all()]
POWERPOINT_CHOICES = [(ppt.count, ppt.count) for ppt in PowerPoint.objects.all() or None]

# # # Create your models here.
class Order(models.Model):
    
    client = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_client")
    topic = models.CharField(max_length=100, help_text="Tell us your topic")
    type_of_paper = models.CharField(choices=PAPER_TYPE_CHOICES,max_length=100)
    discipline = models.CharField(max_length=100, choices=DISCIPLINE_CHOICES)
    pages = models.PositiveBigIntegerField(default=1)
    words = models.PositiveBigIntegerField(default=275)
    academic_level = models.CharField(choices=(
        ("DA", "Dont Apply"),
        ("HS", "High School"),
        ("CG", "College"),
        ("UG", "Undergraduate"),
        ("MS/PDH", "Masters/Phd"),
    ), default="UG", max_length=10)
    deadline = models.DateTimeField(default=timezone.now)
    paper_instruction = models.TextField(blank=True, null=True)
    files = models.FileField(upload_to="orders/", blank=True, null=True)
    paper_format = models.CharField(max_length=100, choices=(
        ("APA", (("APA6", "APA 6"),("APA7", "APA 7"),("APA9", "APA 9"),)),
        ("MLA", "MLA"),
        ("CHICAGO", "Chicago/Turabian"),
        ("NA", "Not Applicable"),
        ("HARVARD", "Harvard"),
        ("OTHER", "OTHER"),
    ), default="APA")
    type_of_service = models.CharField(max_length=10, choices=(
        ("SW", "Sample Writing"),
        ("ER", "Editting Rewriting"),
        ("CALC", "Calculations")
    ), default="SW")
    reference_copies = models.BooleanField(default=False)
    sms_update = models.BooleanField(default=False)
    turnitin_report = models.BooleanField(default=False)
    writer_choice = models.CharField(max_length=2, choices = (
        ("RW", "Regular Writer"),
        ("FW", "First Writer"),
        ("PW", "Professional Writer")
    ), default="RW")
    ppt = models.CharField(max_length=100, choices=POWERPOINT_CHOICES, blank=True, null=True)
    software_tools = models.BooleanField(default=False)
    software_tool_description = models.TextField(blank=True, null=True)
    weekly = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        get_latest_by = "createdAt"
    
    def __str__(self):
        return str(self.topic)
    
    def save(self, *args, **kwargs):
        self.deadline += datetime.timedelta(hours=3)
        return super(Order, self).save(*args, **kwargs)


