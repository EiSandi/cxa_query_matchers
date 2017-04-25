from rest_framework import serializers
from cxa_query.models import *

class EligibilitySerializer(serializers.ModelSerializer):
    class Meta():
        model = Eligibility
        fields = ('description',)
        
    def create(self, validated_data):
        """
        Create and return a new `Eligibility` instance, given the validated data.
        """
        return Eligibility.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Eligibility` instance, given the validated data.
        """
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class AreaCoverageSerializer(serializers.ModelSerializer):
    class Meta():
        model = AreaCoverage
        fields = ('description',)

    def create(self, validated_data):
        """
        Created and return a new `AreaCoverage` instance, given the validated data.
        """
        return AreaCoverage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AreaCoverage` instance, given the validated data.
        """
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class BasicCoverageSerializer(serializers.ModelSerializer):
    class Meta():
        model = BasicCoverage
        fields = ('description',)

    def create(self, validated_data):
        """
        Create and return a new `BasicCoverage` instance, given the validated data.
        """
        return BasicCoverage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update andd return an existing `BasicCoverage` instance, given the validated data.
        """
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    group_eligibility = EligibilitySerializer()
    group_area_coverage = AreaCoverageSerializer()
    group_basic_coverage = BasicCoverageSerializer()

    class Meta():
        model = Group
        fields = ('id','name','group_eligibility','group_area_coverage','group_basic_coverage','category')

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
        instance.group_basic_coverage = validated_data.get('group_basic_coverage', instance.group_basic_coverage)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class GroupEligibilitySerializer(serializers.ModelSerializer):
    group_eligibility = EligibilitySerializer()

    class Meta():
        model = Group
        fields = ('group_eligibility',)

class GroupAreaCoverageSerializer(serializers.ModelSerializer):
    group_area_coverage = AreaCoverageSerializer()

    class Meta():
        model = Group
        fields = ('group_area_coverage',)

class GroupBasicCoverageSerializer(serializers.ModelSerializer):
    group_basic_coverage = BasicCoverageSerializer()

    class Meta():
        model = Group
        fields = ('group_basic_coverage',)


            


