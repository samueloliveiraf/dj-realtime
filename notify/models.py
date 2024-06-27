from django.db import models


class Notification(models.Model):
    order_name = models.CharField(
        max_length=2048
    )
