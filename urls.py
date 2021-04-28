from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from crudapp import views

urlpatterns = [
    path('',views.emp_form,name='employee_insert'),
    path('<int:id>/',views.emp_form,name='employee_update'),
    path('delete<int:id>/',views.emp_delete,name='employee_delete'),
    path('list/',views.emp_list,name='employee_list')

]
