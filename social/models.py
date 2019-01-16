from django.db import models


class Swiped(models.Model):
    FLAGS = (
        ('disklike', '左滑'),
        ('like', '右滑'),
        ('superlike', '上滑'),
    )

    flag = models.CharField(max_length=16, choices=FLAGS, verbose_name='滑动类型')
    uid = models.IntegerField(verbose_name='滑动者的 uid')
    sid = models.IntegerField(verbose_name='被滑动者的 uid')
    stime = models.DateTimeField(auto_now_add=True)
