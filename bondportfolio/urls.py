from django.urls import path
from . import views

urlpatterns = [
    #path('api/bonds', views.BondListCreate.as_view()),
    path('api/bonds', views.BondFilter.as_view(), name='bonds'),
]
