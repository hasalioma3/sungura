from csv import field_size_limit

from pyexpat import model
from rest_framework import serializers

from assets.models import Assets


class AssetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assets
        fields = [
            "category",
            "name",
            "barcode",
            "serialNumber",
            "accessory",
            "location",
        ]
