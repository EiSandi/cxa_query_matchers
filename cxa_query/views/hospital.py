from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import *
from cxa_query.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import os


@api_view(['GET'])
def hospital_list(request):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		if request.method == 'GET':
			hospitals = Hospital.objects.all()
			serializer = HospitalSerializer(hospitals, many=True)
			return Response(serializer.data)
		else:
			return Response({'status':'Token Authentication Failed.'})

@api_view(['GET'])
def hospital_detail(request, pk, format=None):
	if request.GET.get('params') is not None:
		token = request.GET.get('params')
	else:
		token = request.META['HTTP_AUTHORIZATION']

	if token == os.environ.get('TOKEN'):
		if request.method == 'GET':
			hospital = Hospital.objects.get(pk=pk)
			serializer = HospitalDetailsSerializer(hospital)
			return Response(serializer.data)
	else:
		return Response({'status':'Token Authentication Failed.'})
