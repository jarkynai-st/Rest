from api.models import Book
from .models import Comment
from rest_framework.serializers import ModelSerializer

class CommentSetSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class BookDetailSerializer(ModelSerializer):

    comment_set = CommentSetSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id','title','description','price','year','author','comment_set']