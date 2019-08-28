from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'BudgetViewSet',views.FiberBudgetViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
