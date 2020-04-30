"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

"""by allow charge a file in the dirname"""
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('api/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),
    url('api/users/', include('users.urls')),
    url('api/institutions/', include('institutions.urls')),
    url('api/uploads/', include('files.urls')),
    url('api/groups/', include('groups.urls')),
    url('api/courses/', include('courses.urls')),
    url('api/workspaces/', include('workspace.urls')),
    url('api/secctions/', include('secctions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)