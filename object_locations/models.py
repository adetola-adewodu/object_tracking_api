from django.db import models
from django.utils.timezone import now
# Create your models here.


    # block 0: sig: 3 x: 9 y: 183 width: 18 height: 28
# Create your models here.
class Block(models.Model):
    device_id = models.CharField(max_length=64, null=True, blank=True)
    block_id = models.IntegerField()
    signature = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    color = models.CharField(max_length=50, null=True, blank=True)
    width = models.IntegerField()
    height = models.IntegerField()
    status = models.CharField(max_length=50, null=True, blank=True, default="latest")
    timestamp = models.DateTimeField(default=now)
