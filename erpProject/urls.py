"""erpProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from erp_construction.urls import router
#from erp_fiber_ftts.urls import router
from users.urls import router
from inventory.urls import router
from django.conf import settings
from django.conf.urls.static import static

from users.views import ObtainJWTView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view=ObtainJWTView.as_view(), name='login'),
    path('erp_construction/', include('erp_construction.urls')),
    #path('erp_fiber_ftts/', include('erp_fiber_ftts.urls')),
    path('', include('users.urls')),
    path('inventory/', include('inventory.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
