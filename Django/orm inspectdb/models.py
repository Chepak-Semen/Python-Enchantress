# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'country'


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    menu = models.ForeignKey('Menu', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    season = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'menu'


class Personal(models.Model):
    name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    phone = models.CharField(unique=True, max_length=30, blank=True, null=True)
    rest = models.ForeignKey('Restourant', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'


class Restourant(models.Model):
    name = models.CharField(unique=True, max_length=20)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restourant'
