from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import *
from cxa_query.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import os

# class BenefitsList(generics.ListCreateAPIView):
# 	queryset = Benefits.objects.all()
# 	serializer_class = BenefitsSerializer

# class BenefitsDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Benefits.objects.all()
# 	serializer_class = BenefitsSerializer

@api_view(['GET'])
def benefits_list(request):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		if request.method == 'GET':
			benefits = Benefits.objects.all()
			serializer = BenefitsSerializer(benefits, many=True)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def benefits_detail(request, pk, format=None):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		try:
			benefits = Benefits.objects.get(pk=pk)
		except Benefits.DoesNotExist:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = BenefitsSerializer(benefits)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def benefits_basiccoverage(request, pk, format=None):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		if request.method == 'GET':
			benefits = Benefits.objects.get(pk=pk)
			serializer = BenefitsBasicCoverageSerializer(benefits)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def benefits_areacoverage(request, pk, format=None):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		if request.method == 'GET':
			benefits = Benefits.objects.get(pk=pk)
			serializer = BenefitsAreaCoverageSerializer(benefits)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})