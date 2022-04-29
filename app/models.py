from django.db import models


class Item(models.Model):
    property_id = models.CharField(
        max_length=300,
        verbose_name="property_id",
    )

    def __str__(self):
        return self.property_id
