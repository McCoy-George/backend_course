from django.db import models

# Create your models here.

# The `TimestampModel` class is an abstract model that includes fields for creation and update
# timestamps.
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True

# The Category class represents a category with a name and description.
# The `TimestampModel` class is an abstract model that includes fields for creation and
# update timestamps. It has two fields: `created_at` and `updated_at`, both of which
# are `DateTimeField` fields. The `created_at` field is automatically set to the
# current date and time when an instance of the model is created, while the
# `updated_at` field is automatically updated to the current date and time whenever an
# instance of the model is saved. This allows for easy tracking of when a model
# instance was created and last updated.
class Category(TimestampModel):
    category_name = models.CharField(max_length = 180)
    description = models.TextField(max_length = 250)

    def __str__(self):
        """
        The above function returns the category name as a string.
        :return: The `__str__` method is returning the `category_name` attribute of the object.
        """
        return self.category_name

#on delete Model cascade is an option in Django model to specify 
# what should happen when the object reference deleted means if reference 
# object deleted all the object at a foreign key relationship to will also 
# deleted useful for maintaining reference Integrity ensuring that related 
# objects are deleted when the referenced object is deleted
class Product(TimestampModel):
    product_name = models.CharField(max_length=180)
    description = models.TextField(max_length=180)
    price = models.DecimalField(max_digits =10, decimal_places=2)
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 

    def __str__(self):
        return self.product_name

class order(TimestampModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.id}"
    
#models.py file in Django is used to define the structure of the database
#tables and the fields they will contain, It is part of the model
#view template architecture in Django
#and it also responsible for defining the data structures and relationships
#models in the application
#in this file you can define your data models as python classes which are then
#used to create database tables in the backend.
#Each class defines a table and each attribute in the class defines fields
#within our table