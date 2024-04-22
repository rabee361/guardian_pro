from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('test/' , CalenderView.as_view()),
    path('chats/' , Chats.as_view()),
    # path('chat/<str:pk>/' , Chat.as_view()),
    path('chat-messages/<str:chat_id>/', ChatMessages.as_view()),
    path('get-soura/<str:pk>/' , GetSoura.as_view())
]