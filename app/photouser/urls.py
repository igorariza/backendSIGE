from django.urls import path

from .views import (
                    #Picture
                    ProfilePictureUploadView,
                    ProfilePictureDetail,
                    ProfilePictureList,
                    ProfilePictureDelete,
                    ProfilePictureByUser
                    )

urlpatterns = [
    #Picture
    path('create/', ProfilePictureUploadView.as_view()),
    path('', ProfilePictureList.as_view()),
    path('<pk>', ProfilePictureDetail.as_view()),
    path('delete/<pk>', ProfilePictureDelete.as_view()),
    path('picture/', ProfilePictureByUser.as_view())
    ]