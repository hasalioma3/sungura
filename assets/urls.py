from django.urls import path

from .views import AssetViewSet

urlpatterns = [path("", AssetViewSet.as_view({"get": "list"}))]
