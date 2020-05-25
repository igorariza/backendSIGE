from django.urls import path

from .views import (
    
    WorkSpaceList,
    WorkSpaceDetail,
    WorkSpaceCreate,
    WorkSpaceUpdate,
    WorkSpaceDelete,
    WorkSpaceCoursesTeacher,
    WorkSpaceCreateMultiple,
    WorkSpaceOnlySecctions
    
)


urlpatterns = [
    path('', WorkSpaceList.as_view()),
    path('only/secctions/<teacherDictate>', WorkSpaceOnlySecctions.as_view()),
    path('courses/<teacherDictate>/<groupDictate>', WorkSpaceCoursesTeacher.as_view()   ),
    path('create/', WorkSpaceCreate.as_view()),
    path('create/bulk/', WorkSpaceCreateMultiple.as_view()),
    path('<pk>', WorkSpaceDetail.as_view()),
    path('update/<pk>', WorkSpaceUpdate.as_view()),
    #path('delete/<pk>', WorkSpaceDelete.as_view()),
]