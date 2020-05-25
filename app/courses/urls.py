from django.urls import path

from .views import (
    AreaList,
    AreaDetail,
    AreaCreate,
    AreaUpdate,
    AreaDelete,
    AreaCreateMultiple,

    CourseList,
    CourseDetail,
    CourseCreate,
    CourseUpdate,
    CourseDelete,
    CourseCreateMultiple,

    AcademicChargeList,
    AcademicChargeDetail,
    AcademicChargeCreate,
    AcademicChargeUpdate,
    AcademicChargeDelete,
    AcademicChargeCoursesListTeacher,
    AcademicChargeCreateMultiple,
    AcademicChargebyTeacher,
    AcademicChargabyStuden,

    TimeTableList,
    TimeTableDetail,
    TimeTableCreate,
    TimeTableUpdate,
    TimeTableDelete
)

urlpatterns = [
    # Areas
    path('area/', AreaList.as_view()),
    path('area/create/', AreaCreate.as_view()),
    path('area/create/bulk/', AreaCreateMultiple.as_view()),
    path('area/<pk>', AreaDetail.as_view()),
    path('area/update/<pk>', AreaUpdate.as_view()),
    #path('area/delete/<pk>', AreaDelete.as_view()),
    # Courses
    path('course/', CourseList.as_view()),
    path('course/create/', CourseCreate.as_view()),
    path('course/create/bulk/', CourseCreateMultiple.as_view()),
    path('course/<pk>', CourseDetail.as_view()),
    path('course/update/<pk>', CourseUpdate.as_view()),
    #path('coursedelete/<pk>', CourseDelete.as_view()),
    # Academic Charges
    path('academiccharge/', AcademicChargeList.as_view()),
    path('academiccharge/create/', AcademicChargeCreate.as_view()),
    path('academiccharge/create/bulk/', AcademicChargeCreateMultiple.as_view()),
    path('academiccharge/<pk>', AcademicChargeDetail.as_view()),
    path('academiccharge/update/<pk>', AcademicChargeUpdate.as_view()),
    path('academiccharge/delete/<pk>', AcademicChargeDelete.as_view()),
    path('academiccharge/dictategroup/<teacherDictate>', AcademicChargeCoursesListTeacher.as_view()),
    path('academiccharge/byteacher/<teacherDictate>', AcademicChargebyTeacher.as_view()),
    #path('academiccharge/bystudent/<studentEnrollment>', AcademicChargabyStuden.as_view()),

    # Time Table
    path('timetable/', TimeTableList.as_view()),
    path('timetable/create/', TimeTableCreate.as_view()),
    path('timetable/<pk>', TimeTableDetail.as_view()),
    path('timetable/update/<pk>', TimeTableUpdate.as_view()),
    #path('timetable/delete/<pk>', TimeTableDelete.as_view())
]
