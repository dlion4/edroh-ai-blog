from rest_framework import generics


class SerializerListViewMixin(generics.ListAPIView):
    serializer_class = None
    queryset = None


    