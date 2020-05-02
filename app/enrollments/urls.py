from django.urls import path

from .views import (
 
    EnrollmentList,
    EnrollmentDetail,
    EnrollmentCreate,
    EnrollmentUpdate,
    EnrollmentDelete,
    EnrollmentCreateMultiple
    
)

urlpatterns = [
    # Academic Charges
    path('Enrollment/', EnrollmentList.as_view()),
    path('Enrollment/create/', EnrollmentCreate.as_view()),
    path('Enrollment/create/bulk/', EnrollmentCreateMultiple.as_view()),
    path('Enrollment/<pk>', EnrollmentDetail.as_view()),
    path('Enrollment/update/<pk>', EnrollmentUpdate.as_view()),
    path('Enrollment/delete/<pk>', EnrollmentDelete.as_view())
]
