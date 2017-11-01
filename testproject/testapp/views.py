from rest_framework.viewsets import ModelViewSet

from .models import MyTestModel
from .serializers import MyTestModelSerializer


class MyTestModelViewSet(ModelViewSet):
    queryset = MyTestModel.objects.all()
    serializer_class = MyTestModelSerializer
