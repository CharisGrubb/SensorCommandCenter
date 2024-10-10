

import requests 


def get_all_sensors():
    

    response = requests.get("http://127.0.0.1:8000/sensors", headers={'username':"jediMaster", 'password':"R2D2_for_President"})
    print(response)
    if response.status_code == 200:
        results = response.json()
        for r in results['results']:
            print(r)
    else:
        print('Failed to get results...response code:', response.status_code)

