from django.urls import path, re_path

from . import views


urlpatterns = [
	path('', views.homepage, name = 'homepage'),
    path('employeeview', views.employeeview, name = 'employeeview'),
]
