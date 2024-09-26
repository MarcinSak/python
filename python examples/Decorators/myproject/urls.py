from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include app URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Add the login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add the logout view
]
