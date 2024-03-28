from rest_framework import serializers
from task.models import Task
from django.forms import ValidationError


class TaskSerializer(serializers.ModelSerializer):

    # Add additional fields not specifically in model.

    description = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"
    
     #Function for additional field.
    def get_description(self, data):
        return f'Task #{data.id} regarding profit center #{data.profitCenterNumber}'
   