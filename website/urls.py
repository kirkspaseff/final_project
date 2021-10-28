from django.urls import path, re_path

from . import views


urlpatterns = [
	path('', views.homepage, name = 'homepage'),
    path('payroll/', views.payroll, name = 'payroll'),
    path('employeeview', views.employeeview, name = 'employeview'),
    re_path(r'.*', views.other, name = 'bad link')
]
