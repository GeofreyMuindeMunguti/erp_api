# your_app/urls.py
from django.urls import path, include
from rest_framework import routers
from fcm_messaging.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls))

]