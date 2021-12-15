from django.db import models


class Product(models.Model):
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
        default=0.00,
        max_digits=10,
        decimal_places=2,
        help_text="The current price of the product",
    )

    def __str__(self):
        return "%(name)s (%(price)s)" % {"name": self.title, "price": self.price}
