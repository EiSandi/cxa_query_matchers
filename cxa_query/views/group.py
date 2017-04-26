from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import Group
from cxa_query.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class GroupList(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MedicalGroup(generics.ListAPIView):
	queryset = Group.objects.filter(category = 'Medical')
	serializer_class = GroupSerializer

class ProtectionGroup(generics.ListAPIView):
	queryset = Group.objects.filter(category = 'Protection')
	serializer_class = GroupSerializer

class GroupEligibiliy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupEligibilitySerializer

class GroupAreaCoverage(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupAreaCoverageSerializer

class GroupBasicCoverage(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupBasicCoverageSerializer

@api_view(['GET'])
def generate_token(request):
	if request.method == 'GET':
		#cxa_data_metlife
		return Response({'token':'756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121'})

@api_view(['GET'])
def group_list(request):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.all()
			serializer = GroupSerializer(group, many=True)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def group_detail(request, pk, format=None):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		try:
			group = Group.objects.get(pk=pk)
		except Group.DoesNotExist:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = GroupSerializer(group)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def medical_group(request):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.filter(category = 'Medical')
			serializer = GroupSerializer(group, many=True)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def protection_group(request):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.filter(category = 'Protection')
			serializer = GroupSerializer(group, many = True)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def group_eligibility(request, pk, format=None):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.get(pk=pk)
			serializer = GroupEligibilitySerializer(group)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def group_areacoverage(request, pk, format=None):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.get(pk=pk)
			serializer = GroupAreaCoverageSerializer(group)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def group_basiccoverage(request, pk, format=None):
	token = request.META['HTTP_AUTHORIZATION']
	if token == '756395f053e947e8332e6f6b838a409d5e48e226833c05d87ce711de0d441121':
		if request.method == 'GET':
			group = Group.objects.get(pk=pk)
			serializer = GroupBasicCoverageSerializer(group)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

