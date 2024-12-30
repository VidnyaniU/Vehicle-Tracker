from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VehicleTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("vehicle_tracking", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("vehicle_tracking", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "vehicle_tracking",
            {
                "type": "update_location",
                "message": data,
            },
        )

    async def update_location(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
