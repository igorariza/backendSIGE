from django.urls import path

from .views import (
    # Community
    CommunityCreate,
    CommunityDelete,
    CommunityDetail,
    CommunityList,
    CommunityUpdate,
    CommunityListbyIE,
    # File
    AddfileUploadView,
    AddfileDetail,
    AddfileDelete,
    AddfileList,
    AddfileDetail,
    # Replay
    ReplayCreate,
    ReplayDetail,
    ReplayList,
    ReplayUpdate,
    ReplayDelete
)

urlpatterns = [
    # Community
    path('create/', CommunityCreate.as_view()),
    path('', CommunityList.as_view()),
    path('<pk>', CommunityDetail.as_view()),
    path('delete/<pk>', CommunityDelete.as_view()),
    path('upate/<pk>', CommunityUpdate.as_view()),
    path('byIE/<codeIE>', CommunityListbyIE.as_view()),
    # Resource
    path('file/create/', AddfileUploadView.as_view()),
    path('file/', AddfileList.as_view()),
    path('file/<pk>', AddfileDetail.as_view()),
    path('file/delete/<pk>', AddfileDelete.as_view()),
    # Replay
    path('replay/create/', ReplayCreate.as_view()),
    path('replay/', ReplayList.as_view()),
    path('replay/<pk>', ReplayDetail.as_view()),
    path('replay/delete/<pk>', ReplayDelete.as_view()),
    path('replay/update/<pk>', ReplayUpdate.as_view()),
]
