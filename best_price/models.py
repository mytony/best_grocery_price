# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db.models import *


class Product(Model):
    # id = AutoField(primary_key=True)
    title = CharField(max_length=500, default='123', unique=True)
    price = FloatField(default=None)
    category = CharField(max_length=100, default='123', blank=True)
    location = CharField(max_length=100, default='123')

    def __str__(self):
        return self.title

# class Location(Model):
#     name = CharField()
#     address = CharField()
#
#     class Meta():
#         unique_together = ('name', 'address')
#
# https://docs.djangoproject.com/en/1.11/ref/models/fields/#choices
# class ProductAtLocation(Model):
#     price = IntegerField(default=None)
#     unit = CharField()
#     product = ForeignKey(Product)
#     location = ForeignKey(Location)
#
#
# class UserProductType(IntEnum):
#     purchase = 1
#     search = 2
#     browse = 3
#
#     @classmethod
#     def tostring(cls, val):
#         for k,v in vars(cls).iteritems():
#             if v == val:
#                 return k
#
#     @classmethod
#     def fromstring(cls, str):
#         typ = getattr(cls, str.lower(), None)
#         if typ is None:
#             raise IllegalArgumentError('Closet product type %s not recognized.' % str)
#         return typ
#
# class TemplateGenerator(IntEnum):
#     pre_generated = 1
#     season_generator = 100
#
#
# class TemplateLook(Model):
#     product = ForeignKey(Product, null=False, blank=False, related_name='template_looks')
#     timestamp = DateTimeField(default=timezone.now, blank=True, db_index=True)
#     generator = IntegerField(default=int(TemplateGenerator.season_generator), blank=False, null=False)