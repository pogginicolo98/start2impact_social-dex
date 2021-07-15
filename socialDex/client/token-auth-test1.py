from pathlib import Path
import requests
from sys import path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
path.insert(0, str(BASE_DIR))
import password


def client():
    """
    API client.
    Client for test authentication via REST Auth and make a request to an API that require a user authenticated.

    Run the script first with the st.1 uncommented and the st.2 commented, then st.1 commented and st.2 uncommented.
    Steps:
    1 - Authentication with credentials and retrieving authentication token.
    2 - Request to an API endpoint authenticating via token.
    """

    # Step 1
    # ------
    credentials = password.CREDENTIALS_ADMIN
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    # Step 2
    # ------
    # token_h = password.TOKEN_ADMIN
    # headers = {'Authorization': token_h}
    # response = requests.get('http://127.0.0.1:8000/api/posts/', headers=headers)

    # Output
    # ------
    response_data = response.json()
    print('Status code: ', response.status_code)
    print('Response data: ', response_data)


if __name__ == '__main__':
    client()
