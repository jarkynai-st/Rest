from rest_framework.fields import SerializerMethodField

from api.models import Book
from .models import Comment
from rest_framework.serializers import ModelSerializer,Serializer,CharField
from astimate.serializer import RateModelSerializer

class CommentSetSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(Serializer):
    text = CharField(allow_blank=False)


class BookDetailSerializer(ModelSerializer):
    rates = RateModelSerializer(many=True)
    comment_set = CommentSetSerializer(many=True)
    avg_rate = SerializerMethodField()
    sale_price = SerializerMethodField()



    class Meta:
        model = Book
        fields = ['id','title','description','price','year',
                  'author','comment_set','rates','avg_rate','sale','sale_price','sale_amount']


    def get_sale_price(self,obj):
        sale_price = 0
        if obj.sale:
            sale_price = obj.price - (obj.price * obj.sale_amount) / 100
            return sale_price
        return obj.price


    def get_avg_rate(self,obj):
        total_star = 0
        for rate in obj.rates.all():
            total_star += rate.star
        return round(total_star / len(obj.rates.all()),1)