from rest_framework.serializers import ModelSerializer

from .models import MyTestModel


class MyTestModelSerializer(ModelSerializer):
    class Meta:
        model = MyTestModel
        fields = (
            'charfield',
            'datefield',
            'datetimefield',
            'decimalfield',
            'floatfield',
            'id',
            'integerfield',
            'timefield',
            'uuidfield',
        )
