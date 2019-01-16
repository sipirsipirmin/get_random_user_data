from django.urls import path
from egitim import views

urlpatterns = [
    path('', views.RandomUserView.as_view(), name='randomuser'),
]
