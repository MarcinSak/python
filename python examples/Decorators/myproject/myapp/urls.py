from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', views.admin_panel, name='admin_panel'),
]
