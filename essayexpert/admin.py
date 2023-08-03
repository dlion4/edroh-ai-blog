from django.contrib import admin
from .models import (
Discipline,
SubDiscipline,
PaperType,
PowerPoint,
Order,
)


class SubDisciplineInlineAdmin(admin.StackedInline):
    model = SubDiscipline
    extra=0

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        SubDisciplineInlineAdmin,
    ]


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(PowerPoint)
class PowerPointAdmin(admin.ModelAdmin):
    pass



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["topic","type_of_paper","discipline","pages","words","academic_level","deadline","paper_format","type_of_service","reference_copies","sms_update","turnitin_report","writer_choice","ppt","software_tools",]
    search_fields = ['topic', 'type_of_paper', 'discipline', "client"]
    list_filter = [
        "client",
        'discipline',
        'academic_level',
        'paper_format',
        'writer_choice',
        "deadline",
        "weekly"
    ]

