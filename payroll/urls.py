from django.urls import path, re_path

from . import views

app_name='payroll'
urlpatterns = [
	path('', views.payroll, name = 'payroll'),
    path('view', views.viewpayroll, name='viewpayroll'),
    re_path(r'.*', views.other, name = 'bad link')
]