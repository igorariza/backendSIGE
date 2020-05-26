from django.urls import path

from .views import (
 
    EnrollmentList,
    EnrollmentDetail,
    EnrollmentCreate,
    EnrollmentUpdate,
    EnrollmentDelete,
    EnrollmentCreateMultiple,
    EnrollmentListByGroup,
    EnrollmentListByGroupManager
    
)

urlpatterns = [
    # Academic Charges
    path('enrollment/', EnrollmentList.as_view()),
    path('enrollment/create/', EnrollmentCreate.as_view()),
    path('enrollment/create/bulk/', EnrollmentCreateMultiple.as_view()),
    path('enrollment/<pk>', EnrollmentDetail.as_view()),
    path('enrollment/update/<pk>', EnrollmentUpdate.as_view()),
    #path('enrollment/delete/<pk>', EnrollmentDelete.as_view()),
    path('enrollment/byGroup/<groupEnrollment>', EnrollmentListByGroup.as_view()),
    path('enrollment/byGroupmanager/<managerGroup>', EnrollmentListByGroupManager.as_view()),


]
