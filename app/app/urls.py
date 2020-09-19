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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

"""by allow charge a file in the dirname"""


urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/institutions/', include('institutions.urls')),
    path('api/uploads/', include('files.urls')),
    path('api/groups/', include('groups.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/workspaces/', include('workspace.urls')),
    path('api/secctions/', include('secctions.urls')),
    path('api/enrollments/', include('enrollments.urls')),
    path('api/tutorials/', include('tutorials.urls')),
    path('api/profilepictures/', include('photouser.urls')),
    path('api/forum/', include('forum.urls')),
    path('api/images/', include('images.urls')),
    path('api/community/', include('community.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/stadistics/', include('stadistics.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
