from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Logo(models.Model):
    logo = models.ImageField(upload_to="static/img/logo")


class Assets(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    barcode = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    serialNumber = models.CharField(max_length=200, null=True, blank=True)
    accessory = models.BooleanField(default=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )
    transit = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    date_dispatched = models.DateTimeField(auto_now_add=True)
    dispatched = models.BooleanField(default=False)
    deliveryNo = models.CharField(max_length=200, null=True, blank=True)
    fromLocation = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )
    toLocation = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="toLocation",
    )
    # toLocation = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.deliveryNo)

    @property
    def key1(self):
        return str(self.id).zfill(6)

    @property
    def get_delivery_items_no(self):
        deliveryAssetss = self.deliveryAssets_set.all()
        total = sum([Assets.quantity for Assets in deliveryAssetss])
        return total

    def get_delivery_Assetss(self):
        deliveryAssetss = self.deliveryAssets_set.all()
        return deliveryAssetss


class DeliveryAssets(models.Model):
    Assets = models.ForeignKey(Assets, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_dispatched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Assets)

    def get_deliveryNoteNo(self):
        dnn = self.delivery_set.all()
        return dnn
