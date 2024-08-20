import json
# from asgiref.sync import async_to_sync

# from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from .models import Message

# Implementación Síncrona
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.user = self.scope["user"]
#         self.id = self.scope["url_route"]["kwargs"]["course_id"]
#         self.room_group_name = f"chat_{self.id}"
#         # join room group
#         # print(self.channel_name)
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#         # accept connection
#         self.accept()

#     def disconnect(self, close_code):
#         # leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#         pass

#     # receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         # send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 "type": "chat_message",
#                 "message": message,
#                 "user": self.user.username,
#                 "datetime": timezone.now().isoformat(),
#             },
#         )
#         # send message to WebSocket
#         # self.send(text_data=json.dumps({"message": message}))

#     # receive message from room group
#     def chat_message(self, event):
#         # send message to WebSocket
#         self.send(text_data=json.dumps(event))


# Implementación Asíncrona
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        self.room_group_name = f"chat_{self.id}"
        # join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def persist_message(self, message):
        # save message to database
        # using acreate() instead of create() to avoid
        # IntegrityError when multiple messages are sent
        await Message.objects.acreate(
            user=self.user, course_id=self.id, content=message
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": self.user.username,
                "datetime": timezone.now().isoformat(),
            },
        )
        await self.persist_message(message)
        # send message to WebSocket
        # self.send(text_data=json.dumps({"message": message}))

    # receive message from room group
    async def chat_message(self, event):
        # send message to WebSocket
        await self.send(text_data=json.dumps(event))
