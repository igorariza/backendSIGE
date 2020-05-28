from django.urls import path

from .views import (

    EducationalInstitutionList,
    EducationalInstitutionDelete,
    EducationalInstitutionDetail,
    EducationalInstitutionCreate,
    EducationalInstitutionCreateMultiple,
    EducationalInstitutionUpdate,
    EducationalInstitutionInactivate,


    HeadquartersList,
    HeadquartersDetail,
    HeadquartersCreate,
    HeadquartersCreateMultiple,
    HeadquartersUpdate,
    HeadquartersDelete,
    HeadquartersInactivate
)


urlpatterns = [
    path('educationalinstitution/', EducationalInstitutionList.as_view()),
    path('educationalinstitution/create/',
         EducationalInstitutionCreate.as_view()),
    path('educationalinstitution/create/bulk/',
         EducationalInstitutionCreateMultiple.as_view()),
    path('educationalinstitution/<pk>/', EducationalInstitutionDetail.as_view()),
    path('educationalinstitution/update/<pk>/',
         EducationalInstitutionUpdate.as_view()),
    path('educationalinstitution/inactivate/<pk>/',
         EducationalInstitutionInactivate.as_view()),
    #path('educationalinstitution/delete/<pk>',EducationalInstitutionDelete.as_view()),
    path('headquarters/', HeadquartersList.as_view()),
    path('headquarters/create/', HeadquartersCreate.as_view()),
    path('headquarters/create/bulk/', HeadquartersCreateMultiple.as_view()),
    path('headquarters/<pk>', HeadquartersDetail.as_view()),
    path('headquarters/update/<pk>', HeadquartersUpdate.as_view()),
    #path('headquarters/delete/<pk>', HeadquartersDelete.as_view()),
    path('headquarters/inactivate/<pk>/', HeadquartersInactivate.as_view())
]
