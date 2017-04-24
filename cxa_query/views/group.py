from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import Group
from cxa_query.serializers import GroupSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class GroupList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# 	queryset = Group.objects.all()
# 	serializer_class = GroupSerializer

	# def get(self, request, *args, **kwargs):
	# 	return self.list(request, *args, **kwargs)

	# def post(self, request, *args, **kwargs):
	# 	return self.create(request, *args, **kwargs)

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

# @api_view(['GET', 'PUT'])
# def medicalgroup_detail(request, pk):
# 	try:
# 		group = Group.objects.get(pk=pk)
# 	except Group.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = GroupSerializer(group)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = GroupSerializer(group, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
