from django.urls import path

from .views import (
    
    GroupList,
    GroupDetail,
    GroupCreate,
    GroupUpdate,
    GroupDelete,
    
    JourneyList,
    JourneyDetail,
    JourneyCreate,
    JourneyUpdate,
    JourneyDelete
    
)


urlpatterns = [
    path('group/', GroupList.as_view()),
    path('group/create/', GroupCreate.as_view()),
    path('group/<pk>', GroupDetail.as_view()),
    path('group/update/<pk>', GroupUpdate.as_view()),
    path('group/delete/<pk>', GroupDelete.as_view()),
    
    path('journey/', JourneyList.as_view()),
    path('journey/create/', JourneyCreate.as_view()),
    path('journey/<pk>', JourneyDetail.as_view()),
    path('journey/update/<pk>', JourneyUpdate.as_view()),
    path('journey/delete/<pk>', JourneyDelete.as_view())
    
]