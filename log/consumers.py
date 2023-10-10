import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected!")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        self.message_content = data['data']  # 인스턴스 변수로 지정

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

        # Move the import here to avoid circular dependencies
        from .models import log_Message

        # 데이터베이스에 메시지 저장
        message = log_Message(content=self.message_content)  # 인스턴스 변수로부터 값을 가져옴
        message.save()

        # 모든 클라이언트에게 메시지 전송
        await self.send(text_data=json.dumps({
            'data': self.message_content
        }))
