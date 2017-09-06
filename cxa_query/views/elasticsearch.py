from rest_framework import mixins
from rest_framework import generics

from cxa_query.models import Group
from cxa_query.serializers import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import os

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
     from urllib2 import urlparse
     from urllib import urlencode

try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import HTTPError


import json

import urllib2
import urllib

@api_view(['GET','POST'])
def searchpost(request, format=None):

	print(request.data.get('data'))
	post_data = request.data.get('data')
	for x in post_data:
		print x

 # 	baseurl = urllib2.Request('http://localhost:9200/twitter/tweet/_search?q=user:kimchy')
 # 	result = urlopen(baseurl).read()
	# return Response(json.loads(result))

	url = "http://localhost:9200/_search"
	data = {
				"query" : {
					"bool" : {
						"must" : [
							{ "terms" : 
								{ "user" : post_data}
							}
						]
					}
				}
			}

	data = json.dumps(data)
	baseurl = urllib2.Request(url,data)
	baseurl.add_header('Content-Type','application/json')
	result = urlopen(baseurl).read()
	return Response(json.loads(result))

@api_view(['GET'])
def search(request, format=None):
	print(request.META['HTTP_DATA'])
	req_data = request.META['HTTP_DATA']
	
	for x in req_data:
		print x

	baseurl = urllib2.Request('http://localhost:9200/twitter/tweet/_search?q=user:kimchy')
 	result = urlopen(baseurl).read()
	return Response(json.loads(result))


