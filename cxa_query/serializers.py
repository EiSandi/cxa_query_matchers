from rest_framework import serializers
from cxa_query.models import *

# class EligibilitySerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Eligibility
#         fields = ('description',)
        
#     def create(self, validated_data):
#         """
#         Create and return a new `Eligibility` instance, given the validated data.
#         """
#         return Eligibility.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Eligibility` instance, given the validated data.
#         """
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

# class AreaCoverageSerializer(serializers.ModelSerializer):

#     class Meta():
#         model = AreaCoverage
#         fields = ('description',)

#     def create(self, validated_data):
#         """
#         Created and return a new `AreaCoverage` instance, given the validated data.
#         """
#         return AreaCoverage.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `AreaCoverage` instance, given the validated data.
#         """
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

# class BasicCoverageSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = BasicCoverage
#         fields = ('description',)

#     def create(self, validated_data):
#         """
#         Create and return a new `BasicCoverage` instance, given the validated data.
#         """
#         return BasicCoverage.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update andd return an existing `BasicCoverage` instance, given the validated data.
#         """
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

class GroupSerializer(serializers.ModelSerializer):

    class Meta():
        model = Group
        fields = ('id','name','eligibility','area_coverage','basic_coverage','category')

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
        instance.eligibility = validated_data.get('eligibility', instance.eligibility)
        instance.area_coverage = validated_data.get('area_coverage', instance.area_coverage)
        instance.basic_coverage = validated_data.get('basic_coverage', instance.basic_coverage)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class GroupEligibilitySerializer(serializers.ModelSerializer):

    class Meta():
        model = Group
        fields = ('eligibility',)

class GroupAreaCoverageSerializer(serializers.ModelSerializer):

    class Meta():
        model = Group
        fields = ('area_coverage',)

class GroupBasicCoverageSerializer(serializers.ModelSerializer):

    class Meta():
        model = Group
        fields = ('basic_coverage',)

class BenefitsSerializer(serializers.ModelSerializer):

	class Meta():
		model = Benefits
		fields = ('id','name','area_coverage','basic_coverage')

	def create(self, validated_data):
		return Benefits.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.area_coverage = validated_data.get('area_coverage', instance.area_coverage)
		instance.basic_coverage = validated_data.get('basic_coverage',instance.basic_coverage)
		instance.save()
		return instance

class BenefitsBasicCoverageSerializer(serializers.ModelSerializer):

    class Meta():
        model = Benefits
        fields = ('basic_coverage',)

class BenefitsAreaCoverageSerializer(serializers.ModelSerializer):

    class Meta():
        model = Benefits
        fields = ('area_coverage',)

class AdmissionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Admission
        fields = ('description','before_admission','upon_discharge','after_discharge')

class BeforeAdmissionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Admission
        fields = ('before_admission',)

class AdmissionUponDischargeSerializer(serializers.ModelSerializer):

    class Meta():
        model = Admission
        fields = ('upon_discharge',)

class AdmissionAfterDischargeSerializer(serializers.ModelSerializer):

    class Meta():
        model = Admission
        fields = ('after_discharge',)
 


