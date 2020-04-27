from django.urls import path

from .views import (
    
    GroupList,
    GroupDetail,
    GroupCreate,
    GroupUpdate,
    GroupDelete
    
)


urlpatterns = [
    path('', GroupList.as_view()),
    path('create/', GroupCreate.as_view()),
    path('<pk>', GroupDetail.as_view()),
    path('update/<pk>', GroupUpdate.as_view()),
    path('delete/<pk>', GroupDelete.as_view())
]