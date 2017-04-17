from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import AreaCoverage
from cxa_query.serializers import AreaCoverageSerializer

class AreaCoverageList(generics.ListCreateAPIView):
	queryset = AreaCoverage.objects.all()
	serializer_class = AreaCoverageSerializer
