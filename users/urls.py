from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from  . import urls
from django.urls import path, include

from .views import ObtainJWTView

router = DefaultRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('login/', view=ObtainJWTView.as_view(), name='login')
]
