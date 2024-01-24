from django.urls import path
from main import views

urlpatterns = [
    path('', views.product, name='product')
    path('emp/', views.employee,)
]
