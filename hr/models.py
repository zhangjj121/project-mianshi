# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

CHAOXIANG = ((1,'东'),
             (2, '南'),
             (3, '西'),
             (4, '北'),
             (5, '南北'),
             )
class AllMessage(models.Model):
    staffname = models.CharField(max_length=32)
    gender = models.CharField(max_length=6)
    id_number = models.CharField(unique=True, max_length=18, blank=True, null=True)
    telephone = models.CharField(max_length=11)
    region = models.CharField(max_length=16)
    education = models.CharField(max_length=3, blank=True, null=True)
    school = models.CharField(max_length=128, blank=True, null=True)
    graduatet_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_message'


class Password(models.Model):
    user = models.ForeignKey(AllMessage, models.DO_NOTHING, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password'

class FangInfo(models.Model):
    put_person = models.ForeignKey(AllMessage,null=True,verbose_name='录入人')
    xiaoqu = models.CharField(max_length=32,verbose_name='小区',null=False)
    louhao = models.IntegerField(null=False,verbose_name='楼号',default=1)
    danyuan = models.IntegerField(null=False,verbose_name='单元')
    fjnumber = models.IntegerField(null=False,verbose_name='房间号')
    chaoxiang = models.IntegerField(choices=CHAOXIANG,null=False)
    mianji = models.DecimalField(verbose_name='面积',max_digits=7,decimal_places=2)

    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2)


    class Meta:
        db_table='new_fang'

    def __str__(self):
        return self.put_person

    def choice(self):
        if self.chaoxiang == 1:
            return u'东'
        elif self.chaoxiang == 2:
            return u'南'
        elif self.chaoxiang == 3:
            return u'西'
        elif self.chaoxiang == 4:
            return u'北'
        else:
            return u'南北'