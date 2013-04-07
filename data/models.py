from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=200)

    def __unicode__(self):
        return self.ticker