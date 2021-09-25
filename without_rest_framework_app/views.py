from django.shortcuts import render
from django.views.generic import View
from without_rest_framework_app.models import Employee
from without_rest_framework_app.mixins import SerializeMixin, HttpResponseMixin
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from without_rest_framework_app.utils import is_json
from without_rest_framework_app.forms import EmployeeForm


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailsCBV(HttpResponseMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'Error Message': 'The requested data is not found'})
            return self.render_to_http_response(json_data, status=404)
        else:
            json_data = self.serialize([emp])
            return self.render_to_http_response(json_data)

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'Error Message': 'No matched data is found, not able to update'})
            return self.render_to_http_response(json_data, status=404)
        else:
            data = request.body
            valid_jason = is_json(data)
            if not valid_jason:
                json_data = json.dumps({'Error Message': 'Please send valid json data only'})
                return self.render_to_http_response(json_data, status=404)
            else:
                p_data = json.loads(data)
                original_data = {
                    'e_no': emp.e_no,
                    'e_name': emp.e_name,
                    'e_salary': emp.e_salary,
                    'e_address': emp.e_address
                }
                original_data.update(p_data)
                form = EmployeeForm(original_data, instance=emp)
                if form.is_valid():
                    form.save(commit=True)
                    json_data = json.dumps({'Message': 'Resource Updated Successfully'})
                    return self.render_to_http_response(json_data)
                elif form.errors:
                    json_data = json.dumps(form.errors)
                    return self.render_to_http_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'Error Message': 'No matched data is found, not able to delete'})
            return self.render_to_http_response(json_data, status=404)
        else:
            deletion_status, deleted_item = emp.delete()
            if deletion_status == 1:
                json_data = json.dumps({'Message': 'Resource Deleted Successfully'})
                return self.render_to_http_response(json_data)
            else:
                json_data = json.dumps({'Error Message': 'Unable to Delete, Please try again!'})
                return self.render_to_http_response(json_data, status=404)

# ----------------------------------------------------------------------------------------------------------------------


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid_jason = is_json(data)
        if not valid_jason:
            json_data = json.dumps({'Error Message': 'Please send valid json data only'})
            return self.render_to_http_response(json_data, status=404)
        else:
            p_data = json.loads(data)
            form = EmployeeForm(p_data)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'Message': 'Resource Created Successfully'})
                return self.render_to_http_response(json_data)
            elif form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status=400)

# ----------------------------------------------------------------------------------------------------------------------

# Serialization - converting a dict(or any object) to json(any object)

# another method useless, but working is:

        # emp_data = {
        #     'e_no': emp.e_no,
        #     'e_name': emp.e_name,
        #     'e_salary': emp.e_salary,
        #     'e_address': emp.e_address
        # }
        # json_data = json.dumps(emp_data)

# [Method Level]:
# from django.views.decorators.csrf import csrf_exempt ----> @csrf_exempt

# [Class Level]:
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator ----> @method_decorator(csrf_exempt, name='dispatch)

# [Project Level]:
# disable this da: 'django.middleware.csrf.CsrfViewMiddleware' in settings.py

# to POST new data into database, we need forms(internally da!).

# ----------------------------------------------------------------------------------------------------------------------
