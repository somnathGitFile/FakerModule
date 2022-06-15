from django.shortcuts import render, redirect
from.models import Employee
from faker import Faker
import random

# Create your views here.
def ShowEmployee(request):
    template_name='CRUDAPP/showEmp.html'
    data=Employee.objects.all()
    context={'obj':data}
    return render(request,template_name,context)

def FakeEmployeeData(request):
    fake=Faker()
    for i in range(5):
        emp=Employee()

        emp.eid=random.randint(0,999)
        emp.ename=fake.name()
        emp.esal=random.randint(20000,90000)
        emp.city=fake.city()

        emp.save()
    return redirect('showEmp_url')



