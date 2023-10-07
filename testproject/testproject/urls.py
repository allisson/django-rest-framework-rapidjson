from django.urls import include, path

urlpatterns = [
    path(r"^test/", include("testapp.urls")),
]
