from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# from . import urls
from django.conf.urls import url, include

router = DefaultRouter()

router.register(r'procurementcost', views.procurementcostViewSet)


urlpatterns = [
    url('', include(router.urls)),
]
