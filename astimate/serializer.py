from rest_framework import serializers
from .models import Rate

class RateSerializer(serializers.Serializer):

    star = serializers.IntegerField(min_value=0,max_value=10)


class RateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['id','star']