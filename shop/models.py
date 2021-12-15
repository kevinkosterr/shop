import uuid

from django.db import models
from shop.modules.tools import _update_or_create


class FeatureManager(models.Manager):
    update_or_create = _update_or_create


class Feature(models.Model):
    """A feature is data that should be inserted into the database at the start of the application.

    It's data required to properly run/set up the application."""

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50, null=False, blank=False, help_text="Name of the feature."
    )
    author = models.CharField(
        max_length=20, null=False, blank=False, help_text="Author of the feature."
    )
    contact = models.EmailField(
        null=True,
        blank=True,
        help_text="Author's e-mail-address for contacting about implemented feature.",
    )
    installation_ts = models.DateTimeField(
        name="Installation Timestamp",
        null=True,
        blank=True,
        help_text="Time the feature was installed.",
    )
    installed = models.BooleanField(
        default=False, help_text="Whether the feature was installed or not."
    )
    reference = models.CharField(
        null=True, blank=True, help_text="Reference to a PR or issue on GitHub."
    )
    # overwriting the 'objects' property to feature the update_or_create feature.
    objects = FeatureManager()

    def __str__(self):
        return f"{self.name} [{str(self.installation_ts) if self.installed else 'Not installed'}]"


class Product(models.Model):
    """Model for products"""

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text="Title/name of the product",
    )
    description = models.TextField(
        max_length=300,
        null=False,
        help_text="Product's description",
    )
    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text="The current price of the product",
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%(name)s (%(price)s)" % {"name": self.title, "price": self.price}
