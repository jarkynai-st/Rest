from django.urls import path
from .views import *

urlpatterns = [

    path('rate/<int:book_id>/',RateView.as_view())

]