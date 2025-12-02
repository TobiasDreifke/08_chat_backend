from urllib import request
from django.urls import path
from .views import ChatView, RedirectToChatView, chat_detail

urlpatterns = [
    path("", ChatView.as_view(), name="chat-view"),
    path("detail/<int:chat_id>/", chat_detail, name="detail-chat"),
    path("<slug:chat_slug>/", RedirectToChatView.as_view()),
    path("chat/<slug:chat_slug>/", RedirectToChatView.as_view(), name="chat_slug_url"),
]