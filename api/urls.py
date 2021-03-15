from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('order_set',OrderModelViewSet)
router.register('books',BookView)


urlpatterns = [

    path('user/',UserView.as_view()),
    path('authors/',AuthorView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('',include(router.urls)),
    path('my_orders/',MyOrdersAPIView.as_view()),
    path('branchs/',BranchAPIView.as_view()),
    path('contacts/',ContactView.as_view()),
    path('order/<int:order_id>/',ModifyOrder.as_view()),
    path('book_demo/<str:abbr>/',BookDemoView.as_view()),

]