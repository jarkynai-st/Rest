from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *
# Create your views here.
from .token import account_activation_token


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class RegisterConfirmView(APIView):

    def post(self,request,*args,**kwargs):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "OGOGO PYTHON Inc."
            message = render_to_string('accounts/acc_active_email.html', {
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = serializers.data['email']
            email = EmailMessage(subject=mail_subject, body=message, to=[to_email,])
            email.send()
            return HttpResponse({"data":"Succesfully"})
        return Response(serializers.errors)


def activate(request, uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.is_staff = True
        user.save()
        login(request,user)
        return HttpResponse({"OKAY!"})
    return Response({"NOT OKAY"})