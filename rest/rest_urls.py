from django.conf.urls import url,include

from rest_framework import routers

from rest.rest_views import *
from rest.views import saltrun_list,saltrun_detail


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hostname', HostnameView)
router.register(r'species', SpeciesView)
router.register(r'saltrun', SaltrunView)


"""
rest api就是已经封装了.所以你写一个url就是注册一个.但是rest api封装的url必须得跟django的url结合起来,那就通过  url(r'^', include(router.urls)), 方式
"""

'''
 url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 是认证
'''

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^saltrun_list/$', saltrun_list),
    url(r'^saltrun_detail/(\d+)/$', saltrun_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]