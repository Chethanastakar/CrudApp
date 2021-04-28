from django.shortcuts import render,redirect
from .forms import EmployeeForm
from crudapp.models import Employee
# Create your views here.
def emp_form(request,id=0):
    if(request.method=='GET'):
        if(id==0):
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)   #filtering based on primary key
            form=EmployeeForm(instance=employee)  #on clicking edit coming here
        return render(request,'emp_form.html',{'form':form})  #first it will come here
    else:
        request.method=='POST' #post request
        if(id==0):
            form=EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)  #after edit giving submit coming here
        if(form.is_valid()):
            form.save()
        return redirect('/employee/list')



def emp_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,'emp_list.html',context)
def emp_delete(request,id):
    #delete based on
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
