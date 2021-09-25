import json
import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_request(id):
    resp = requests.get(BASE_URL + END_POINT + id + '/')
    print('Status Code: ', resp.status_code)
    print(resp.json())


# id = input('Enter Employee Id: ')
# get_request(id)

# ----------------------------------------------------------------------------------------------------------------------

def get_all():
    resp = requests.get(BASE_URL + END_POINT)
    print('Status Code: ', resp.status_code)
    print(resp.json())


# get_all()

# ----------------------------------------------------------------------------------------------------------------------


def create_resource():
    new_emp = {
        'e_no': '700',
        'e_name': 'Harshita Lingapalem',
        'e_salary': 75000,
        'e_address': 'Banglore'
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(new_emp))
    print('Status Code: ', resp.status_code)
    print(resp.json())


# create_resource()

# ----------------------------------------------------------------------------------------------------------------------

def update_resource(id):
    new_emp = {
        'e_salary': 75000,
        'e_address': 'Bangalore'
    }
    resp = requests.put(BASE_URL + END_POINT + str(id) + '/', data=json.dumps(new_emp))
    print('Status Code: ', resp.status_code)
    print(resp.json())

# update_resource(400)

# ----------------------------------------------------------------------------------------------------------------------

def delete_resource(id):
    resp = requests.delete(BASE_URL + END_POINT + str(id) + '/')
    print('Status Code: ', resp.status_code)
    print(resp.json())

delete_resource(7)

# ----------------------------------------------------------------------------------------------------------------------

# "if resp.status_code in range(200, 300)" or "if resp.status_code == requests.codes.ok"

# STATUS_CODES:
# 1XX ----> Informational
# 2XX ----> Successful
# 3XX ----> Redirection
# 4XX ----> Client Error
# 5XX ----> Server Error

# python manage.py dumpdata without_rest_framework_app.Employee --indent 4
# python manage.py dumpdata without_rest_framework_app.Employee --format xml --indent 4
# python manage.py dumpdata without_rest_framework_app.Employee --format xml > emp.xml --indent 4
# python manage.py dumpdata without_rest_framework_app.Employee > emp.json --indent 4

# ----------------------------------------------------------------------------------------------------------------------
