from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register_set',RegisterView)

urlpatterns = [

    path('',include(router.urls)),
    path('register/',RegisterConfirmView.as_view()),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate,name='activate'),
]