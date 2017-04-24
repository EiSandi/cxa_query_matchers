"""cxa_query_matchers URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cxa_query import views
from rest_framework import routers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('cxa_query.urls'))
    url(r'^group/$', views.GroupList.as_view()),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),

    url(r'^eligibility/$', views.EligibilityList.as_view()),
    url(r'^area/$', views.AreaCoverageList.as_view()),
    url(r'^basic-coverage/$', views.BasicCoverageList.as_view()),
    url(r'^basic-coverage/(?P<pk>[0-9]+)/$', views.BasicCoverageDetail.as_view()),

    url(r'^medical/$', views.MedicalGroup.as_view()),
    url(r'^protection/$', views.ProtectionGroup.as_view())
    # url(r'^medical/(?P<pk>[0-9]+)/$', views.medicalgroup_detail)

]