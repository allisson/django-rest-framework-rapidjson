
from django.db import models


class MyTestModel(models.Model):
    charfield = models.CharField(max_length=255)
    datefield = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(decimal_places=2, max_digits=10)
    floatfield = models.FloatField()
    integerfield = models.IntegerField()
    timefield = models.TimeField()
    uuidfield = models.UUIDField()
