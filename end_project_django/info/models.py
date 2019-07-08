# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InfoHostinfo(models.Model):
    host = models.CharField(max_length=32)
    count = models.IntegerField()
    start_time = models.DateTimeField()
    is_lock = models.CharField(max_length=32)

    class Meta:
        #managed = False
        db_table = 'info_hostinfo'


class TInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    marry = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    academic = models.CharField(max_length=255, blank=True, null=True)
    nation = models.CharField(max_length=255, blank=True, null=True)
    politics = models.CharField(max_length=255, blank=True, null=True)
    exper = models.CharField(max_length=255, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    census = models.CharField(max_length=255, blank=True, null=True)
    job_status = models.CharField(max_length=255, blank=True, null=True)
    job_addr = models.CharField(max_length=255, blank=True, null=True)
    job_p = models.CharField(max_length=255, blank=True, null=True)
    job_ind = models.CharField(max_length=255, blank=True, null=True)
    job_salary = models.CharField(max_length=255, blank=True, null=True)
    edu = models.TextField(blank=True, null=True)
    null1 = models.CharField(max_length=255, blank=True, null=True)
    null2 = models.CharField(max_length=255, blank=True, null=True)
    null3 = models.CharField(max_length=255, blank=True, null=True)
    null4 = models.CharField(max_length=255, blank=True, null=True)
    null5 = models.CharField(max_length=255, blank=True, null=True)
    job_exp = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 't_info'


class TLog(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    func = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        #managed = False
        db_table = 't_log'


class TUser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    null = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 't_user'
