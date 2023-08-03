from rest_framework import generics
from essayexpert.models import (
    Discipline,
    SubDiscipline,
    PaperType,
    PowerPoint,
    Order,
)
from .serializers import (
    DisciplineSerializer,
    SubDisciplineSerializer,
    PaperTypeSerializer,
    PowerPointSerializer,
    OrderSerializer,
)

class OrderSerializerView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()