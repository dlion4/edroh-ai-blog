from rest_framework import generics
from .mixins import SerializerListViewMixin

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


class OrderSerializerView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class DesciplineSerializerView(SerializerListViewMixin):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()


class PaperTypeSerializerView(SerializerListViewMixin):
    serializer_class = PaperTypeSerializer
    queryset = PaperType.objects.all()
