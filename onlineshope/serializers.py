
# The `OrderSerializer` class is a serializer for the `order` model that includes all fields.
from rest_framework import serializers
from .models import order


# The OrderSerializer class is a serializer for converting Order objects to JSON format.
class OrderSerializer(serializers.ModelSerializer):

   # The above class is a Meta class that specifies the model and fields for an order.
    class Meta:
        model = order
       # The `fields = '__all__'` statement in the `OrderSerializer` class specifies that all fields
       # of the `order` model should be included in the serialized representation of an order object.
       # This means that when an order object is serialized using this serializer, all fields of the
       # order model will be included in the resulting JSON representation.
        fields = '__all__'
        
#Serializers defines a structure of a data that is
#to be send and receive by the API
#It converts the complex data types such as Django models
#into python data type that can be easily rendered into 
#a JSON or other content type

#Serializers also validate incoming data ensuring that it meets 
#the requirements defined in the serializer class it also handles
#the conversion of python data types into a JSON or other content type
#for sending to the client
