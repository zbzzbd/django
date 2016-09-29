# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title =     models.CharField(u'标题',max_length=256)
    content=    models.TextField(u'内容')

    pub_data=   models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time=models.DateTimeField(u'更新时间',auto_now_add=True,null=True)

    def __unicode__(self):
        return self.title