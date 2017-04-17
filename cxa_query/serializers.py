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

class AreaCoverageSerializer(serializers.ModelSerializer):
    class Meta():
        model = AreaCoverage
        fields = ('id','area')

    def create(self, validated_data):
        """
        Created and return a new `AreaCoverage` instance, given the validated data.
        """
        return AreaCoverage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AreaCoverage` instance, given the validated data.
        """
        instance.area = validated_data.get('area', instance.name)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    group_eligibility = EligibilitySerializer()
    group_area_coverage = AreaCoverageSerializer()

    class Meta():
        model = Group
        fields = ('id','name','group_eligibility','group_area_coverage',)

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
        instance.group_eligibility = validated_data.get('group_eligibility', instance.group_eligibility)
        instance.group_area_coverage = validated_data.get('group_area_coverage', instance.group_area_coverage)
        instance.save()
        return instance


