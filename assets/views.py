from django.shortcuts import render
from rest_framework import viewsets

from assets.models import Assets

from .serializers import AssetsSerializer

# Create your views here.


class AssetViewSet(viewsets.ModelViewSet):
    """Äpi endpint to view all Assets"""

    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer
