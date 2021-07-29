from accounts.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, render


def signup_view(request):
    """
    View function for sign up new users.
    """

    if request.method == 'POST':
        print(request.POST)
        # Bound session, compiled form
        form = SignUpForm(request.POST)
        if form.is_valid():
            # User registration
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        # New session, empty form
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
