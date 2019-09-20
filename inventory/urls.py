from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# from . import urls
from django.urls import path, include

router = DefaultRouter()

router.register(r'procurementcost', views.procurementcostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
