from rest_framework import serializers
from fields.models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title')
