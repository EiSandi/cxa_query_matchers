from rest_framework import serializers
from cxa_query.models import *

class EligibilitySerializer(serializers.ModelSerializer):
    class Meta():
        model = Eligibility
        fields = ('id','description',)
        
    def create(self, validated_data):
        """
        Create and return a new `Eligibility` instance, given the validated data.
        """
        return Eligibility.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Eligibility` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
        
class GroupSerializer(serializers.ModelSerializer):
    group_eligibility = EligibilitySerializer()
    class Meta():
        model = Group
        fields = ('id','name','group_eligibility',)

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
        instance.group_eligibility = validated_data.get('group_eligibility',instance.group_eligibility)
        instance.save()
        return instance


