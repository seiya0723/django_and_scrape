from django.db import models


class Topic(models.Model):

    name    = models.CharField(verbose_name="名前",max_length=30)
    comment = models.CharField(verbose_name="コメント",max_length=2000)

