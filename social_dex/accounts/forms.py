from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    A form class for sign up new users.

    * username, password1, password2 and email are required.
    * password1 and password2 must match.
    """

    username = UsernameField(
        max_length=25,
        label='',
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
        help_text="Max 25 characters. Letters, digits and ./+/-/_ only.",
    )
    email = forms.CharField(
        max_length=45,
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    password1 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirm password'}),
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        # Setting the model class and parameters in order to generate the relative forms
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
    """
    A form for authenticating users.

    * username and password are required.
    * username and password must match with user's credentials.
    """

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        max_length=25,
        label='',
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    A form that lets a user change their password by entering their old password.

    * old_password, new_password1 and new_password2 are required.
    * old_password must match with user's credentials.
    * new_password1 and new_password2 must match.
    """

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'placeholder': 'Current password'}),
    )
    new_password1 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirm password'}),
        help_text="Enter the same password as before, for verification.",
    )


class CustomPasswordResetFrom(PasswordResetForm):
    """
    A form that lets a user reset their password authenticating via email.

    * email is required.
    """

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetFrom, self).__init__(*args, **kwargs)

    email = forms.CharField(
        max_length=45,
        label='',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        help_text="Enter the email associated with your account.",
    )


class CustomSetPasswordForm(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old password.

    * new_password1 and new_password2 are required.
    * new_password1 and new_password2 must match.
    """

    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        max_length=30,
        label='',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Enter the same password as before, for verification.",
    )
