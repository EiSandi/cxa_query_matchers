from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import Group
from cxa_query.serializers import GroupSerializer

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