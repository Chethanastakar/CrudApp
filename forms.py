from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('empid','empname','designation','position')
        labels={'empname':'Emp name',
                'empid':'Emp id'}
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='select'
        self.fields['designation'].required=False
