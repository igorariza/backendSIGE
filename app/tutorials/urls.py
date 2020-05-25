from django.urls import path

from .views import (
    
    TutorialsList,
    TutorialsDetail,
    TutorialsCreate,
    TutorialsUpdate,
    TutorialsDelete,
    TutorialsCreateMultiple,
    
)


urlpatterns = [
    path('', TutorialsList.as_view()),
    path('create/', TutorialsCreate.as_view()),
    path('create/bulk/', TutorialsCreateMultiple.as_view()),
    path('<pk>', TutorialsDetail.as_view()),
    path('update/<pk>', TutorialsUpdate.as_view()),
    #path('delete/<pk>', TutorialsDelete.as_view()),
]