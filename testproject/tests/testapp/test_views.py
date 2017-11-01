from decimal import Decimal
from uuid import uuid4

import pytest
from django.utils.timezone import now
from rest_framework.reverse import reverse
from rest_framework import status

from testapp.models import MyTestModel

pytestmark = pytest.mark.django_db


@pytest.fixture
def my_test_model_data():
    return {
        'charfield': 'charfield',
        'datefield': now().date().isoformat(),
        'datetimefield': now(),
        'decimalfield': Decimal('100.00'),
        'floatfield': float(100.00),
        'integerfield': 100,
        'timefield': now().time(),
        'uuidfield': uuid4()
    }


def test_create(client, my_test_model_data):
    url = reverse('testapp:mytestmodel-list')

    response = client.post(url, my_test_model_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    for field in my_test_model_data:
        assert field in response.data


def test_list(client, my_test_model_data):
    url = reverse('testapp:mytestmodel-list')
    MyTestModel.objects.create(**my_test_model_data)

    response = client.get(url, format='json')
    assert len(response.data) == 1
    for field in my_test_model_data:
        assert field in response.data[0]
