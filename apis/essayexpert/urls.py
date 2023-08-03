from django.urls import path
from .views import (
    OrderSerializerView
)

urlpatterns = [
    path("order/", OrderSerializerView.as_view())
]
