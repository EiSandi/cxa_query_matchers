from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import BasicCoverage
from cxa_query.serializers import BasicCoverageSerializer

class BasicCoverageList(generics.ListCreateAPIView):
	queryset = BasicCoverage.objects.all()
	serializer_class = BasicCoverageSerializer