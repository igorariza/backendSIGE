from django.urls import path

from .views import (
                    #Community
                    CommunityCreate,
                    CommunityDelete,
                    CommunityDetail,
                    CommunityList,
                    CommunityUpdate,
                    CommunityListbyIE
                    )

urlpatterns = [
    #Community
    path('create/', CommunityCreate.as_view()),
    path('', CommunityList.as_view()),
    path('<pk>', CommunityDetail.as_view()),
    #path('delete/<pk>', CommunityDelete.as_view()),
    path('upate/<pk>', CommunityUpdate.as_view()),
    path('byIE/<codeIE>', CommunityListbyIE.as_view())
    ]