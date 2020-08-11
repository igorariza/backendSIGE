from django.urls import path

from .views import (
    # Feed
    FeedCreate,
    FeedDelete,
    FeedDetail,
    FeedList,
    FeedUpdate,
    FeedListbyIE,
    FeedListbyAcademicCharge,
    # File
    File_forumUploadView,
    File_forumDetail,
    File_forumDelete,
    File_forumList,
    File_forumDetail,
    # Replay_feed_forum
    Replay_feed_forumCreate,
    Replay_feed_forumDetail,
    Replay_feed_forumList,
    Replay_feed_forumUpdate,
    Replay_feed_forumDelete
)

urlpatterns = [
    # Feed
    path('create/', FeedCreate.as_view()),
    path('', FeedList.as_view()),
    path('<pk>', FeedDetail.as_view()),
    path('delete/<pk>', FeedDelete.as_view()),
    path('update/<pk>', FeedUpdate.as_view()),
    path('byIE/<codeIE>', FeedListbyIE.as_view()),
    path('byAcademicCharge/<codeAcademicCharge>', FeedListbyAcademicCharge.as_view()),
    # Resource
    path('file/create/', File_forumUploadView.as_view()),
    path('file/', File_forumList.as_view()),
    path('file/<pk>', File_forumDetail.as_view()),
    path('file/delete/<pk>', File_forumDelete.as_view()),
    # Replay_feed_forum
    path('replay_feed_forum/create/', Replay_feed_forumCreate.as_view()),
    path('replay_feed_forum/', Replay_feed_forumList.as_view()),
    path('replay_feed_forum/<pk>', Replay_feed_forumDetail.as_view()),
    path('replay_feed_forum/delete/<pk>', Replay_feed_forumDelete.as_view()),
    path('replay_feed_forum/update/<pk>', Replay_feed_forumUpdate.as_view()),
]
