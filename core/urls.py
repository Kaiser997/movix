from django.urls import path

from core.views import PersonListAPIView

urlpatterns = [
    path("patients/", PersonListAPIView.as_view(), name="patients")
]