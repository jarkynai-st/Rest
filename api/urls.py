from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('order_set',OrderModelViewSet)


urlpatterns = [

    path('user/',UserView.as_view()),
    path('books/',BookView.as_view()),
    path('authors/',AuthorView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('',include(router.urls)),
    path('my_orders/',MyOrdersAPIView.as_view()),
    path('branchs/',BranchAPIView.as_view()),
    path('contacts/',ContactView.as_view()),
    path('order/<int:order_id>/',ModifyOrder.as_view()),

]