import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatRoomConsumer(AsyncWebsocketConsumer):
    total_connections = 0
    async def connect(self):
        """Create and accept connection. Creates a group name for the
        chatroom and adds the group to the channel layer group"""
        type(self).total_connections += 1
        print(type(self).total_connections)
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = f"chat_{self.room_name}"
        print(self.room_name)
        print(self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name)
        
        await self.accept()

        # Increment the user count and check if it's the second user
        user_count = type(self).total_connections
        if user_count == 2:
            await self.send_user_connected_message()

    async def disconnect(self, code):
        """Remove websocket instance from the group"""
        type(self).total_connections -= 1
        username = self.scope.get("user").username if self.scope.get("user") else "Anonymous"
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_message",
                "message": "left the chat",
                "username": username,
            }
        )

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
        if message == "joined":
            await self.send(
                text_data=json.dumps(
                    {
                        "type": "joined",
                    }
                )
            )

    async def send_user_connected_message(self):
        """Send a message to indicate that the second user has connected"""
        username = self.scope.get("user").username if self.scope.get("user") else "Anonymous"
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_message",
                "message": "joined",
                "username": username,
            },
        )