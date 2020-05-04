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
    path('enrollment/', EnrollmentList.as_view()),
    path('enrollment/create/', EnrollmentCreate.as_view()),
    path('enrollment/create/bulk/', EnrollmentCreateMultiple.as_view()),
    path('enrollment/<pk>', EnrollmentDetail.as_view()),
    path('enrollment/update/<pk>', EnrollmentUpdate.as_view()),
    path('enrollment/delete/<pk>', EnrollmentDelete.as_view())
]
