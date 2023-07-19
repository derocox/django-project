from django.urls import path
from .views import ClienteList, ClienteDetail


from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('api/cliente/', ClienteList.as_view(), name='cliente-list'),
    path('api/cliente/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
]