from django.urls import path
from egitim import views

urlpatterns = [
    path('', views.OkulView.as_view(), name='okul'),
    path('sikimsonikurl/',
        views.SikimsonikView.as_view(),
        name='sikimsonikname',
    )
]
