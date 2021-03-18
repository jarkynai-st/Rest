

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
from .serializer import *
from rest_framework import views
# Create your views here.

class UserView(views.APIView):

    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




class AuthorView(views.APIView):

    def get(self,request,*args,**kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':'OK'})
        return Response(serializer.errors)


class OrderAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        return Response({
                    "id": 1,
                    "user": 1,
                    "book": 2,
                    "address": "Lalaland",
                    "date_created": "2021-03-05T16:49:28.748633+06:00",
                    "status": "pending"
                        })

    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ModifyOrder(views.APIView):


    def put(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['order_id'])
        hours = timezone.now().hour * 60
        minutes = timezone.now().minute
        result1 = hours + minutes
        result2 = (order.date_created.hour * 60) + order.date_created.minute
        serializer = OrderSerializer(order,data=request.data)
        print(abs(result1 - result2))
        if serializer.is_valid():
            if (result1 - result2) <= 5:
                serializer.save()
                return Response({"data":"OK!!"})
            else:
                return Response({"data":"Time is up!"})
        return Response(serializer.errors)


    def delete(self,request,order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({'date':'successfully deleted!'})

class MyOrdersAPIView(views.APIView):

    def get(self,request,*args,**kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BookDemoView(views.APIView):

    def get(self,request,*args,**kwargs):
        try:
            book = Book.objects.get(abbr=kwargs['abbr'])
        except Book.DoesNotExist:
            return Response({"data":"Book not found!"},status=status.HTTP_404_NOT_FOUND)
        demo = book.book_file.open()
        return Response({"demo":demo.read()[:5]})


class BranchAPIView(views.APIView):

    def get(self,request,*args,**kwargs):
        branchs = Branch.objects.all()
        serializer = BranchSerializer(branchs, many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ContactView(views.APIView):

    def get(self,request,*args,**kwargs):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)