from django import forms
from without_rest_framework_app.models import Employee


class EmployeeForm(forms.ModelForm):

    def clean_e_salary(self):
        input_salary = self.cleaned_data['e_salary']
        if input_salary < 10000:
            raise forms.ValidationError('The minimum salary of a given employee should be 10000')
        else:
            return input_salary

    class Meta:
        model = Employee
        fields = '__all__'
