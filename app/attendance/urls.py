from django.urls import path

from .views import *

urlpatterns = [
    # Attendance
    path('create/', AttendanceCreate.as_view()),
    path('', AttendanceList.as_view()),
    path('<pk>', AttendanceDetail.as_view()),
    path('delete/<pk>', AttendanceDelete.as_view()),
    path('update/<pk>', AttendanceUpdate.as_view()),
]
