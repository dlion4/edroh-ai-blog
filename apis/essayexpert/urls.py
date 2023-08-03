from django.urls import path
from .views import (
    OrderSerializerView,
    DesciplineSerializerView,
    PaperTypeSerializerView,
    # OrderRetrieveUpdateDestroyApiView,
    OrderRetrieveApiView,
    OrderDeleteApiView,
    OrderUpdateApiView
)

urlpatterns = [
    path("order/", OrderSerializerView.as_view()),
    path("discipline/", DesciplineSerializerView.as_view()),
    path("paper-type/", PaperTypeSerializerView.as_view()),
    path("order/<int:order_id>/", OrderRetrieveApiView.as_view()),
    path("order/<int:order_id>/delete/", OrderDeleteApiView.as_view()),
    path("order/<int:order_id>/update/", OrderUpdateApiView.as_view()),
]
