from django.db import models


class APIKey(models.Model):
    key = models.TextField(primary_key=True)
    active = models.BooleanField(default=False)

    class Meta:
        db_table = "APIkeys"
