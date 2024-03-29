from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Ссылка для активации была отправлена на Ваш электронный адрес'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Пожалуйста, подтвердите свой адрес электронной почты, чтобы завершить регистрацию')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Благодарим вас за подтверждение по электронной почте. Теперь вы можете войти в свою учетную запись')
    else:
        return HttpResponse('Ссылка для активации недействительна!')
