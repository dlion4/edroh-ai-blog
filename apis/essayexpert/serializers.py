from rest_framework import serializers
from essayexpert.models import (
    Discipline,
    SubDiscipline,
    PaperType,
    PowerPoint,
    Order,
)

class SubDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDiscipline
        fields = "__all__"


class DisciplineSerializer(serializers.ModelSerializer):
    sub_discipline = SubDisciplineSerializer(many=True, read_only=True)
    class Meta:
        model = Discipline
        fields = ["id", "name", "sub_discipline"]

class PaperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperType
        fields = ['id', 'name', 'price']

class PowerPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPoint
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id","client","topic","type_of_paper","discipline","pages","words",
            "academic_level","deadline","paper_instruction","files","paper_format",
            "type_of_service","reference_copies","sms_update","turnitin_report",
            "writer_choice","ppt","software_tools","software_tool_description",
            "weekly",
        ]




