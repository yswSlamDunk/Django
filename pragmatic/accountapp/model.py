from django.db import models


class Hello_world(models.Model):
    text = models.CharField(max_length = 255, null = False)