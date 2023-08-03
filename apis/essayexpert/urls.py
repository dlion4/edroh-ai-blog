from django.urls import path
from .views import (
    OrderSerializerView,
    DesciplineSerializerView,
    PaperTypeSerializerView
)

urlpatterns = [
    path("order/", OrderSerializerView.as_view()),
    path("discipline/", DesciplineSerializerView.as_view()),
    path("paper-type/", PaperTypeSerializerView.as_view())
]
