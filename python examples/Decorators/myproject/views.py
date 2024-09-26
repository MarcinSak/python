from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')
