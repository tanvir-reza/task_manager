from rest_framework import serializers
from tasks.models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'