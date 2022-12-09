from peewee import *
from os import path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection,"shop.db"))

# Users
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db
User.create_table(fail_silently=True)

# Products
class Product(Model):
    name = CharField()
    price = CharField()
    class Meta:
        database = db
Product.create_table(fail_silently=True)

