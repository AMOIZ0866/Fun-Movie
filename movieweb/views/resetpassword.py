from django.core.mail import send_mail
from django.db.models import Q
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import TemplateView

from movieweb.models import Signup
from movieweb.serialization import CreateUserSerializer


def ResetPasswordView(request):
    template_name = 'movieweb/password/password_reset.html'
    data = request.POST.get("email", )
    associated_users = Signup.objects.filter(Q(email=data))
    if associated_users.exists():
        for user in associated_users:
            subject = "Password Reset Requested"
            email_template_name = "movieweb/password/password_reset_subject.txt"
            c = {
                "email": user.email,
                'domain': '127.0.0.1:8000',
                'site_name': 'Website',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                'token': user.email,
                'protocol': 'http',
            }
            email = render_to_string(email_template_name, c)
            try:
                send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
            except BadHeaderError:
                return render(request, 'movieweb/password/home.html')
            return render(request, 'movieweb/password/password_reset_done.html')
    return render(request, 'movieweb/password/password_reset.html')


class UpdatePassword(TemplateView):
    def post(self, request, token, *args, **kwargs):
        data = request.POST.get("password", )
        pick_record = Signup.objects.filter(Q(email=token)).first()
        serializer = CreateUserSerializer(pick_record, data={'password': data}, partial=True)
        if serializer.is_valid():
            serializer.save()
        return redirect("login")

