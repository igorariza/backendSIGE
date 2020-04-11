from django.urls import path

from .views import (

    Login,
    UserList, 
    UserDetail,
    UserCreate, 
    UserUpdate,
    UserDelete,

    TeacherList, 
    TeacherDetail,
    TeacherCreate,
    TeacherCreateMultiple,
    TeacherUpdate,
    TeacherDelete,
    
    StudentList, 
    StudentDetail,
    StudentCreate,
    StudentCreateMultiple,
    StudentUpdate,
    StudentDelete,
    
    RelativeList, 
    RelativeDetail,
    RelativeCreate,
    RelativeCreateMultiple,
    RelativeUpdate,

    StaffList,
    StaffDetail,
    StaffCreate,
    StaffCreateMultiple,
    StaffUpdate,
    StaffDelete
)


urlpatterns = [

    path('', UserList.as_view()),
    path('login/', Login.as_view()),
    path('create/', UserCreate.as_view()),
    path('teacher/', TeacherList.as_view()),
    path('teacher/create/', TeacherCreate.as_view()),
    path('teacher/create/bulk/', TeacherCreateMultiple.as_view()),
    path('teacher/<pk>/', TeacherDetail.as_view()),
    path('teacher/<pk>/update/', TeacherUpdate.as_view()),
    path('teacher/<pk>/delete/', TeacherDelete.as_view()),
    path('student/', StudentList.as_view()),
    path('student/create/', StudentCreate.as_view()),
    path('student/create/bulk/', StudentCreateMultiple.as_view()),
    path('student/<pk>/', StudentDetail.as_view()),
    path('student/<pk>/update/', StudentUpdate.as_view()),
    path('student/<pk>/delete/', StudentDelete.as_view()),
    path('relative/', RelativeList.as_view()),
    path('relative/create/', RelativeCreate.as_view()),
    path('relative/create/bulk/', RelativeCreateMultiple.as_view()),
    path('relative/<pk>/', RelativeDetail.as_view()),
    path('relative/<pk>/update/', RelativeUpdate.as_view()),
    path('staff/', StaffList.as_view()),
    path('staff/create/', StaffCreate.as_view()),
    path('staff/create/bulk/', StaffCreateMultiple.as_view()),
    path('staff/<pk>', StaffDetail.as_view()),
    path('staff/<pk>/update', StaffUpdate.as_view()),
    path('staff/<pk>/delete', StaffDelete.as_view()),
    path('<pk>/', UserDetail.as_view()),
    path('<pk>/update/', UserUpdate.as_view()),
    path('<pk>/delete/', UserDelete.as_view())
]