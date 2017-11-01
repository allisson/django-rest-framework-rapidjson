import pytest
from rest_framework.reverse import reverse
from rest_framework import status

from testapp.models import MyTestModel

pytestmark = pytest.mark.django_db


@pytest.fixture
def my_test_model_data():
    return {
        'charfield': 'charfield',
        'datefield': '2017-01-01',
        'datetimefield': '2017-01-01T00:00:00Z',
        'decimalfield': '100.00',
        'floatfield': 100.00,
        'integerfield': 100,
        'timefield': '00:00:00',
        'uuidfield': '6293fec0-6323-4e99-ad42-327b407ffd0f'
    }


def test_create(client, my_test_model_data):
    url = reverse('testapp:mytestmodel-list')

    response = client.post(url, my_test_model_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    for field in my_test_model_data:
        assert response.data[field] == my_test_model_data[field]


def test_list(client, my_test_model_data):
    url = reverse('testapp:mytestmodel-list')
    MyTestModel.objects.create(**my_test_model_data)

    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    for field in my_test_model_data:
        assert response.data[0][field] == my_test_model_data[field]
