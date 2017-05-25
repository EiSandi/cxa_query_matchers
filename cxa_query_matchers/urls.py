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

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CXA QUERY MATCHER API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),

    #WITHOUT TOKEN
    # url(r'^api/admin/group/$', views.GroupList.as_view()),
    # url(r'^api/admin/group/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),
    # url(r'^api/admin/benefits/$', views.BenefitsList.as_view()),
    # url(r'^api/admin/benefits/(?P<pk>[0-9]+)/$', views.BenefitsDetail.as_view()),

    # # url(r'^group/(?P<pk>[0-9]+)/eligibility/$', views.GroupEligibiliy.as_view()),
    # # url(r'^group/(?P<pk>[0-9]+)/area/$', views.GroupAreaCoverage.as_view()),
    # # url(r'^group/(?P<pk>[0-9]+)/basic/$', views.GroupBasicCoverage.as_view()),

    # url(r'^eligibility/$', views.EligibilityList.as_view()),
    # url(r'^area/$', views.AreaCoverageList.as_view()),
    # url(r'^basic-coverage/$', views.BasicCoverageList.as_view()),
    # url(r'^basic-coverage/(?P<pk>[0-9]+)/$', views.BasicCoverageDetail.as_view()),

    # # url(r'^medical/$', views.MedicalGroup.as_view()),
    # # url(r'^protection/$', views.ProtectionGroup.as_view()),

    # #WITH TOKEN
    url(r'token/$', views.generate_token),
    url(r'^group/$', views.group_list),
    url(r'^group/(?P<pk>[0-9]+)/$', views.group_detail),
    url(r'^medical/$', views.medical_group),
    url(r'^protection/$', views.protection_group),
    url(r'^group/(?P<pk>[0-9]+)/eligibility/$', views.group_eligibility),
    url(r'^group/(?P<pk>[0-9]+)/area/$', views.group_areacoverage),
    url(r'^group/(?P<pk>[0-9]+)/basic/$', views.group_basiccoverage),

    url(r'^benefit/$', views.benefits_list),
    url(r'^benefit/(?P<pk>[0-9]+)/$', views.benefits_detail),
    url(r'^benefit/(?P<pk>[0-9]+)/basic/$', views.benefits_basiccoverage),
    url(r'^benefit/(?P<pk>[0-9]+)/area/$', views.benefits_areacoverage),

    url(r'^admissions/$', views.admission_list),
    url(r'^admissions/(?P<pk>[0-9]+)/$', views.admission_detail),
    url(r'^admissions/(?P<pk>[0-9]+)/before/$', views.admission_beforeadmission),
    url(r'^admissions/(?P<pk>[0-9]+)/upon/$', views.admission_upondischarge),
    url(r'^admissions/(?P<pk>[0-9]+)/after/$', views.admission_afterdischarge),

    # url(r'^search/(?P<name>[\w\-]+)/$', views.search),
    url(r'^searchpost/$', views.searchpost),
    url(r'^search/$', views.search)

]