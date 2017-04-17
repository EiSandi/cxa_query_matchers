from rest_framework import serializers
from cxa_query.models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta():
        model = Group
        fields = ('id','name',)

    def create(self, validated_data):
        """
        Create and return a new `Group` instance, given the validated data.
        """
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Group` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance