from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include

from .views import ObtainJWTView

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'chat', views.ChatViewSet)
router.register(r'emailserver', views.EmailConfigViewSet)
router.register(r'email', views.SentEmailViewSet)
router.register(r'Log', views.LogViewSet)

router.register(r'location', views.LocationViewSet)
router.register(r'casuals', views.CasualViewSet)
router.register(r'enginners', views.EngineerViewSet)

router.register(r'rates', views.RatesViewSet)

router.register(r'permissions', views.PermissionMapViewSet)
router.register(r'contenttype', views.ContentTypeViewSet)

router.register(r'TeamMemberType', views.TeamMemberTypeViewSet)
router.register(r'projectteamftts', views.ProjectTeamFTTSViewSet)
router.register(r'projectteamftth', views.ProjectTeamFTTHViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]
