from urllib import request
from django.urls import path
from .views import ChatView, RedirectToChatView, single_chat_int_view


urlpatterns = [
    path("", ChatView.as_view(), name="chat-view"),
    path("<slug:chat_slug>", RedirectToChatView.as_view()),
    path("chat/<slug:chat_slug>", RedirectToChatView.as_view(), name ="chat_slug_url"),
    path("<int:chat_id>", single_chat_int_view, name="single-chat"),
]
