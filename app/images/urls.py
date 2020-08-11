from django.urls import path

from .views import (
    ImageResponseList,
    ImageResponseDetail,
    ImageResponseDelete,
    ImageResponseCreate
)


urlpatterns = [
    path('', ImageResponseList.as_view()),
    path('<pk>', ImageResponseDetail.as_view()),
    path('delete/<pk>', ImageResponseDelete.as_view()),
    path('create/', ImageResponseCreate.as_view()),
]
