from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserForm
from .models import Profile

import requests


def register(request):
    '''
    Register a new user
    '''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'] # First retrieve email
            username = email.split("@")[0] # Then use email to get username
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            
            # Create user
            user = Profile.objects.create_user(
                email = email,
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name,
            )
            user.phone_number = phone_number
            user.save()

            # Send activation mail
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('profiles/verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Activation link sent to your email!')
            return redirect('/profiles/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'profiles/register.html', context)


def login(request):
    '''
    Logging in a user
    '''
    if request.method == "POST":
        email       = request.POST['email']
        password    = request.POST['password']
        user        = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful!')
            url = request.META.get('HTTP_REFERER')
            try:
                query   = requests.utils.urlparse(url).query
                params  = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials.')
            return redirect('login')
    return render(request, 'profiles/login.html')


@login_required(login_url = 'login')
def logout(request):
    '''
    Logout a user.
    '''
    auth.logout(request)
    messages.success(request, 'Loggout Successful!')
    return redirect('login')


def activate(request, uidb64, token):
    '''
    Activating a user account.
    '''
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Profile._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Profile.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account is activated!')
        return redirect('login')
    else:
        messages.error(request, 'invalid activation link')
    return redirect('register')


@login_required(login_url='login')
def dashboard(request):
    '''
    Displaying the user Dashboard
    '''
    profile = request.user # Directly use the logged-in user
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/dashboard.html', context)


def reset_password(request):
    '''
    For reseting the user password
    '''
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Profile.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('reset_password')
    else:
        return render(request, 'profiles/reset_password.html')


@login_required(login_url='login')
def edit_profile(request):
    '''
    To edit the user details
    '''
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'profiles/edit_profile.html', {'user_form': user_form})


@login_required(login_url='login')
def change_password(request):
    '''
    For changing user password
    '''
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = Profile.objects.get(username__exact=request.user.username)

        if new_password == confirm_new_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password is now updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Your current password is not correct!')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('change_password')

    return render(request, 'profiles/change_password.html')
