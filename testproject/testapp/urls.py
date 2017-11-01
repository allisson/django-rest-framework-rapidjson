from rest_framework import routers

from .views import MyTestModelViewSet

app_name = 'testapp'
router = routers.SimpleRouter()
router.register(r'my-test-model', MyTestModelViewSet)
urlpatterns = router.urls
