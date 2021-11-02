from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User


from userprofile.models import Employee
from .models import Payroll


def payroll(request):
    employees = Employee.objects.all()

    if request.method=='POST':
        try:
            employee_name = request.POST.get('employee_name')
            user = User.objects.get(username=employee_name)
            employee = Employee.objects.get(user=user)
            payroll_id = employee.payroll_set.first().id
            return redirect('payroll:viewpayroll', payroll_id)
        except ValueError:
            return render(request, 'payroll/payroll.html', {'employees': employees, 'error': 'Please make a valid selection.'}) 
    else:
        return render(request, 'payroll/payroll.html', {'employees': employees})

def viewpayroll(request, payroll_id):
    paystub = get_object_or_404(Payroll, pk=payroll_id)
    return render(request, 'payroll/payrolldetail.html', {'paystub':paystub})


def other(request):
    return HttpResponse("Bad Page!")