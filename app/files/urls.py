from django.urls import path

from .views import (
                    #file
                    FileUploadView,
                    FileDetail,
                    FileList,
                    FileDelete,
                    #evidence
                    EvidenceCreate,
                    EvidenceDelete,
                    EvidenceDetail,
                    EvidenceList,
                    EvidenceUpdate
                    )

urlpatterns = [
    #file
    path('file/', FileUploadView.as_view()),
    path('', FileList.as_view()),
    path('<pk>', FileDetail.as_view()),
    path('delete/<pk>', FileDelete.as_view()),
    #evidence
    path('evidence/create/', EvidenceCreate.as_view()),
    path('evidence/', EvidenceList.as_view()),
    path('evidence/<pk>', EvidenceDetail.as_view()),
    path('evidence/delete/<pk>', EvidenceDelete.as_view()),
    path('evidence/upate/<pk>', EvidenceUpdate.as_view())
    ]