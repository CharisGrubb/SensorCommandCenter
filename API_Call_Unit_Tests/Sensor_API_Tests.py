

import requests 

#FILL OUT
valid_user_name = ''
valid_password = ''
invalid_user_name = ''
invalid_password = ''



def get_all_sensors():
    
    response = requests.get("http://127.0.0.1:8000/sensors", headers={'username':valid_user_name, 'password':valid_password})
    print('RESPONSE',response, response.json())
    if response.status_code == 200:
        results = response.json()
        for r in results['results']:
            print(r)
    else:
        print('Failed to get results...response code:', response.status_code)

def get_specific_sensor():
    pass

def add_sensor():
    pass

#loop through all sensor api endpoint options and test giving them bad creds, ensure correct code is returned
def test_endpoints_with_invalid_creds():
    endpoints = ['/sensors']


get_all_sensors()