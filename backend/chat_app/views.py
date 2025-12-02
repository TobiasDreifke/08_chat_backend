from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, Http404
from django.urls import reverse
from .models import Chat
import json
from django.views import View
from django.utils.text import slugify
from django.views.generic.base import RedirectView
from django.core import serializers
import logging
logger = logging.getLogger(__name__)


class ChatView(View):
    def get(self, request):
        chats = list(Chat.objects.values())
        return JsonResponse(chats, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")

            chat = Chat.objects.create(
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
                message=data.get("message", "")
            )

            chats = list(Chat.objects.values())
            return JsonResponse(chats, safe=False)

        except:
            return JsonResponse({"response": "Das war wohl nichts"})


class RedirectToChatView(RedirectView):
    pattern_name = "chat_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        chat_id = kwargs.get("chat_id")
        chat = get_object_or_404(Chat, id=chat_id)
        slug = slugify(chat.first_name + " " + chat.last_name)
        print(slugify({{chat.first_name}}+" "+{{chat.last_name}}))
        return super().get_redirect_url(chat_slug=slug)


# def single_chat_int_view(request, chat_id):
#     chat = get_object_or_404(Chat, id=chat_id)
#     if len(chat) > chat_id:
#         new_slug = slugify(chat[chat_id]["name"])
#         new_url = reverse("chat_slug_url", args=[new_slug])
#         return redirect(new_url)
#     return HttpResponseNotFound("not found by me")

def single_chat_int_view(request, chat_id):
    logger.info("single_chat_int_view called with %s", chat_id)
    print("single_chat_int_view called with", chat_id)
    chat = get_object_or_404(Chat, id=chat_id)
    json_data = serializers.serialize("json", [chat])
    return HttpResponse(json_data, content_type="application/json")