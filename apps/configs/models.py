import time
from django.db import models

class User(models.Model):
    sign = models.CharField(max_length=32, verbose_name='签名')
    username = models.CharField(max_length=20, verbose_name="用户名")
    create_time = models.IntegerField(default=time.time, blank=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"用户: {self.username} 签名: {self.sign}"


class Config(models.Model):
    uid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nickname = models.TextField(max_length=32, default='匿名', verbose_name="作者")
    title = models.TextField(verbose_name='标题')
    desc = models.TextField(verbose_name='描述')
    config = models.TextField(default='{}', verbose_name='配置文件')

    user_like = models.ManyToManyField(User, blank=True, related_name='user_like', verbose_name='点赞数')
    create_time = models.IntegerField(default=time.time, blank=True, verbose_name='创建时间')
    last_download = models.IntegerField(default=time.time, blank=True, verbose_name='最后下载时间')


    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'昵称: {self.nickname}\n' \
               f'标题: {self.title}\n' \
               f'描述: {self.desc}\n' \
               f'时间: {self.create_time}\n'

