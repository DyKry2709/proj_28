import pytest
import requests
from api.api import auth_token, create_booking

# Тесты с токеном

@pytest.mark.xfail
@pytest.mark.required_token
@pytest.mark.parametrize(
    'auth_token, create_booking, content_type, expected_status',
    [(auth_token(), create_booking(auth_token), 'application/json', 201),      #Действительный токен и данные, позитивный тест
     ('asd324sda', create_booking(auth_token), 'application/json', 403),       #Недействительный токен и действительные данные, негативный тест
     (auth_token(), '-1', 'application/json', 405),                            #Недействительный bookingid и действительные данные, негативный тест
     (auth_token(), create_booking(auth_token), 'text/plain', 415)])           #Недействительные Content-Type and действительные данные, негативный тест
def test_delete_booking(auth_token, create_booking, content_type, expected_status):

    url = f'https://restful-booker.herokuapp.com/booking/{create_booking}'
    headers = {
        'Content-Type': f'{content_type}',
        'Cookie': f'token={auth_token}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 201:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Created', 'Delete booking response should contain "Created"'
    elif response.status_code == 403:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Forbidden', 'Delete booking response should contain "Created"'
    elif response.status_code == 405:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Method Not Allowed', 'Delete booking response should contain "Created"'
    elif response.status_code == 415:
        assert response.status_code == expected_status, f'Delete booking request failed with status code {response.status_code}'
        assert response.text == 'Unsupported Media Type', 'Delete booking response should contain "Created"'