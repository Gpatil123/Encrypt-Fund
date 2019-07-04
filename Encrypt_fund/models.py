from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(max_length=300, null=True, unique=True)

    def __str__(self):
        return self.email