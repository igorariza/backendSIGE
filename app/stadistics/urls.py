from django.urls import path

from .views import *

urlpatterns = [
    # Registros por IE
    
    # usuarios
    path('amount_users/<codeIE>', AmountUserByInstitutio.as_view()),
    path('amount_teachers/<codeIE>', AmountTeachersByInstitutio.as_view()),
    path('amount_students/<codeIE>', AmountStudentsByInstitutio.as_view()),

    # Registros por sede
    path('amount_headquarters/<ieHeadquarters>', AmountHeadquartersByIE.as_view()),
    
    # academica
    path('amount_courses/<head>', AmountDictateCoursesByHead.as_view()),
    
    # usuarios
    path('amount_users/headquarter/<codeHeadquarters>', AmountUserByHeadquarter.as_view()),
    path('amount_teachers/headquarter/<codeHeadquarters>', AmountTeachersByHeadquarter.as_view()),
    path('amount_students/headquarter/<codeHeadquarters>', AmountStudentsByHeadquarter.as_view()),
    

    # Docentes por sede, con las materias que dicta
    path('headquarters_academic_charge_by_teacher/<head>', TeacherAcademic_charge_Head.as_view()),

]


