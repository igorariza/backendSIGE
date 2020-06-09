from django.urls import path

from .views import (
    # Resource
    ResourceUploadView,
    ResourceDetail,
    ResourceList,
    ResourceDelete,
    # HyperLynks
    HyperLynksCreate,
    HyperLynksDelete,
    HyperLynksDetail,
    HyperLynksList,
    HyperLynksUpdate,
    # Secction
    SecctionCreate,
    SecctionDelete,
    SecctionDetail,
    SecctionList,
    SecctionUpdate,
    # ResponseSecction
    ResponseSecctionUploadView,
    ResponseSecctionDetail,
    ResponseSecctionList,
    ResponseSecctionUpdate,
    ResponseSecctionDelete,
    ResponseSecctionStudentDetail,
    # Commnet
    CommentCreate,
    CommentDetail,
    CommentList,
    CommentUpdate,
    CommentDelete
)

urlpatterns = [
    # Resource
    path('resource/create/', ResourceUploadView.as_view()),
    path('resource/', ResourceList.as_view()),
    path('resource/<pk>', ResourceDetail.as_view()),
    #path('resource/delete/<pk>', ResourceDelete.as_view()),
    # HyperLynks
    path('hyperLynks/create/', HyperLynksCreate.as_view()),
    path('hyperLynks/', HyperLynksList.as_view()),
    path('hyperLynks/<pk>', HyperLynksDetail.as_view()),
    #path('hyperLynks/delete/<pk>', HyperLynksDelete.as_view()),
    path('hyperLynks/upate/<pk>', HyperLynksUpdate.as_view()),
    # Secctions
    path('secction/create/', SecctionCreate.as_view()),
    path('secction/', SecctionList.as_view()),
    path('secction/<pk>', SecctionDetail.as_view()),
    #path('secction/delete/<pk>', SecctionDelete.as_view()),
    path('secction/update/<pk>', SecctionUpdate.as_view()),
    # Response
    path('responsesecction/create/', ResponseSecctionUploadView.as_view()),
    path('responsesecction/', ResponseSecctionList.as_view()),
    path('responsesecction/<pk>', ResponseSecctionDetail.as_view()),
    path('responsesecction/<secctionResponse>/<studentResponse>',
         ResponseSecctionStudentDetail.as_view()),
    #path('responsesecction/delete/<pk>', ResponseSecctionDelete.as_view()),
    path('responsesecction/update/<pk>', ResponseSecctionUpdate.as_view()),
    # Comment
    path('commentsecction/create/', CommentCreate.as_view()),
    path('commentsecction/', CommentList.as_view()),
    path('commentsecction/<pk>', CommentDetail.as_view()),
    #path('responsesecction/delete/<pk>', CommentDelete.as_view()),
    path('commentsecction/update/<pk>', CommentUpdate.as_view()),
]
