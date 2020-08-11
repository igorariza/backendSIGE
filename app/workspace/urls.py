from django.urls import path

from .views import (
    
    WorkSpaceList,
    WorkSpaceDetail,
    WorkSpaceCreate,
    WorkSpaceUpdate,
    WorkSpaceDelete,
    WorkSpaceCoursesTeacher,
    WorkSpaceByAcademicCharge,
    WorkSpaceCreateMultiple,
    WorkSpaceOnlySecctions,
    WorkSpaceDetailCourse,
    WorkSpaceDetailStudentCourse,
    
)


urlpatterns = [
    path('', WorkSpaceList.as_view()),
    path('by-academiccharge/<codeAcademicCharge>', WorkSpaceByAcademicCharge.as_view()),
    path('only/secctions/<teacherDictate>', WorkSpaceOnlySecctions.as_view()),
    path('coursedetailteacher/<academicCharge>', WorkSpaceDetailCourse.as_view()),
    path('coursedetailstudent/<academicCharge>', WorkSpaceDetailStudentCourse.as_view()),
    path('courses/<teacherDictate>/<groupDictate>', WorkSpaceCoursesTeacher.as_view()),
    path('create/', WorkSpaceCreate.as_view()),
    path('create/bulk/', WorkSpaceCreateMultiple.as_view()),
    path('<pk>', WorkSpaceDetail.as_view()),
    path('update/<pk>', WorkSpaceUpdate.as_view()),
    #path('delete/<pk>', WorkSpaceDelete.as_view()),
]