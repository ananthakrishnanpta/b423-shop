from django.db import models

# Create your models here.

# Every model which inherits from models.Model, (Model class from the models module from django.db)
# will create a table by name <app_name>_<model_class_name> in the db.
# For eg, here Product class will get a table called mainapp_product in the db.
# After creating, altering or removing any class definition or object variable here,
# we need to run two commands.
# 1. To generate the migration scripts - `python manage.py makemigrations <app_name>`
# 2. To run the migration scripts      - `python manage.py migrate`
# This generates and runs the necessary SQL DDL statements automatically depending on the DB config

class Product(models.Model):
    title  = models.CharField(max_length=200) # This becomes VARCHAR(200)
    price = models.PositiveIntegerField() # This becomes INT with check value >= 0
    desc = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return f"Product : {self.title} for Rs. {self.price}."


