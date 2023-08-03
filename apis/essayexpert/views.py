from rest_framework import generics
from .mixins import SerializerListViewMixin
from rest_framework import status
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
from rest_framework.response import Response

# create
class OrderSerializerView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    # perform
    def perform_create(self, serializer):
        # perform validation
        if serializer.is_valid():
            serializer.save()
            return super(OrderSerializerView, self).perform_create(serializer)
        return Response({"data": serializer.errors})

"""
GET REQUEST
"""

class DesciplineSerializerView(SerializerListViewMixin):
    serializer_class = DisciplineSerializer
    queryset = Discipline.objects.all()


class PaperTypeSerializerView(SerializerListViewMixin):
    serializer_class = PaperTypeSerializer
    queryset = PaperType.objects.all()


"""
UPDATE/POST REQUEST

"""
# class OrderRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
#     serializer_class = OrderSerializer
    
#     def get_object(self, *args, **kwargs):
#         url_pk_kwargs = kwargs.get("order_id")
              
#         return Response({"data": url_pk_kwargs})
    
    
class OrderRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self,request, *args, **kwargs):
        return Order.objects.filter(pk=kwargs.get("order_id")).latest()
    
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset(request,*args, **kwargs)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    
       
class OrderDeleteApiView(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self,request, *args, **kwargs):
        return Order.objects.filter(pk=kwargs.get("order_id")).latest()
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_queryset(request,*args, **kwargs)
        serializer = self.serializer_class(instance)
        instance.delete()
        return Response(serializer.data)


    

        
class OrderUpdateApiView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self,request, *args, **kwargs):
        return Order.objects.filter(pk=kwargs.get("order_id")).latest()
    
    def put(self, request, *args, **kwargs):
        instance = self.get_queryset(request,*args, **kwargs)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


