# from rest_framework import serializers
# from location.models import Location

# # This code defines how the JSON response from the SQL DB is set up.
# class LocationSerializer(serializers.Serializer):
#     profitCenterNumber = serializers.IntegerField()
#     name = serializers.CharField()
#     city = serializers.CharField()
#     state = serializers.CharField()
#     zipCode = serializers.IntegerField()

#     def create(self, data):
#         return Location.objects.create(**data)

#     def update(self, instance, data):
#         instance.profitCenterNumber = data.get('profitCenterNumber', instance.profitCenterNumber)
#         instance.name = data.get('name', instance.name)
#         instance.city = data.get('city', instance.city)
#         instance.state = data.get('state', instance.state)

#         instance.save()
#         return instance

from rest_framework import serializers
from location.models import Location
from django.forms import ValidationError


class LocationSerializer(serializers.ModelSerializer):

    # Add additional fields not specifically in model.

    description = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = "__all__"

    # Self validation function to keep unwanted instances out of the DB.
    def validate_profitCenterNumber(self, value):
        if value == 9999:
            raise ValidationError('Do not enter 4 9s')
        return value
    
    # Validation for data.
    def validate(self, data):
        if data['state'] != 'OK' and data['city'] != 'Weatherford':
            raise ValidationError('This is a data validation test for the model serializer')
        return data
    
    # Function for additional field.
    def get_description(self, data):
        return f'The name of this location is {data.name} and it is profit center #{data.profitCenterNumber}'
    