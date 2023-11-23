import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Create and accept connection. Creates a group name for the
        chatroom and adds the group to the channel layer group"""
        self.group_name = "group_chat_gfg"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        """Remove websocket instance from the group"""
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name)

    async def receive(self, text_data):
        """Receive messages from WebSockets"""

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_message",
                "message": message,
                "username": username,
            },
        )

    async def send_message(self, event):
        """Receive message from room group"""

        message = event["message"]
        username = event["username"]
        # send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )
