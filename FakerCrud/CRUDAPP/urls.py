from django.urls import path
from.import views

urlpatterns=[
    path('SE/', views.ShowEmployee, name='showEmp_url'),
    path('FE/', views.FakeEmployeeData, name='fakeEmp_url'),
]