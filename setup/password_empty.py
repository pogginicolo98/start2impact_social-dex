# settings.py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_django_secret_key'
# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'your_email_host'
EMAIL_PORT = 0
EMAIL_HOST_USER = 'your_email_host_user'
EMAIL_HOST_PASSWORD = 'your_host_password'
DEFAULT_FROM_EMAIL = 'your_email_host_user'
DEFAULT_TO_EMAIL = 'your_email_host_user'

# wallet.py, utils.py
network_url = 'your_network_address'
address = 'your_wallet_address'
private_key = 'your_private_key'

# token-auth-test1.py, token-auth-test2.py
# API client credentials
CREDENTIALS_ADMIN = {'username': 'existing_admin_user', 'password': 'existing_admin_user_password'}
TOKEN_ADMIN = 'Token admin_token'
DATA_USER = {'username': 'luigi3', 'email': 'luigi3.test@mail.com', 'password1': 'Change_me_123$', 'password2': 'Change_me_123$'}
CREDENTIALS_USER = {'username': 'resttest', 'password': 'Change_me_123$'}
TOKEN_USER = 'Token resttest_token'


