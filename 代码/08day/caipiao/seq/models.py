# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TblHeros(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    gender = models.CharField(max_length=64, blank=True, null=True)
    type = models.ForeignKey('TblTypes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_heros'


class TblLianjia(models.Model):
    pic = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    houseinfo = models.CharField(max_length=255, blank=True, null=True)
    positioninfo = models.CharField(db_column='positionInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dealhousetxt = models.CharField(max_length=255, blank=True, null=True)
    dealcycleeinfo = models.CharField(max_length=255, blank=True, null=True)
    agentinfolist = models.CharField(max_length=255, blank=True, null=True)
    dealdate = models.CharField(max_length=255, blank=True, null=True)
    totalprice = models.CharField(max_length=255, blank=True, null=True)
    unitprice = models.CharField(db_column='unitPrice', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_lianjia'


class TblMovies(models.Model):
    rank = models.CharField(max_length=10, blank=True, null=True)
    pic = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    actor = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_movies'


class TblSeq(models.Model):
    red = models.CharField(max_length=255, blank=True, null=True)
    blue = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_seq'


class TblTypes(models.Model):
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_types'
