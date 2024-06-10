from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('add_item/', views.add_item, name='add_item'),
]

