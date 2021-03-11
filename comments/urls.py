from django.urls import path
from .views import *

urlpatterns = [

    path('book/<int:book_id>/',BookDetailView.as_view())
]