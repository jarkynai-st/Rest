from django.shortcuts import render
from rest_framework.response import Response

from .models import Rate,Book
from .serializer import RateSerializer
from rest_framework import views

class RateView(views.APIView):

    def post(self,request,*args,**kwargs):
        book = Book.objects.get(id=kwargs['book_id'])
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            star = serializer.data.get('star')
            Rate.objects.create(book=book,star=star)
            return Response({"data":"thank you for rating!"})
        return Response(serializer.errors)