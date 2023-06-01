import json
from channels.generic.websocket import AsyncWebsocketConsumer
#ეს გამოიყენება კომუნიკაციისთვის მონაცემებთან მაშინ როცა ვარ ასინქრუნლად
from asgiref.sync import sync_to_async
from .models import Room, Messages, User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = 'chat_%s' % self.room_id

        #ანუ რაც აქ გავაკეთეთ ეს ძირითადად ანუ არის რო შევქმენთ ახალი გრუპი რომელიც გამოიყენებს ამ კონსუმერს
        await self.channel_layer.group_add(
            self.room_group_id,
            #ეს მიუთითებს იმ ჩანელ ლეირეზე სეთინგებში რო გვაქ
            self.channel_name
        )

        await self.accept()
    
    #ვიღბთ მესიჯს
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #ეს ჩვენი გამოგზავნილი მესიჯი
        message = text_data_json['message']
        messageUser = text_data_json['messageUser']
        avatarUrl = text_data_json['avatarUrl']
        messageCreated = text_data_json['messageCreated']
        roomId = text_data_json['roomId']

        await self.save_message(messageUser, roomId, message)

        await self.channel_layer.group_send(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message,
                'messageUser': messageUser,
                'avatarUrl': avatarUrl,
                'messageCreated': messageCreated,
                'roomId': roomId,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        messageUser = event['messageUser']
        avatarUrl = event['avatarUrl']
        messageCreated = event['messageCreated']
        roomId = event['roomId']

        await self.send(text_data=json.dumps({
            'message': message,
            'messageUser': messageUser,
            'avatarUrl': avatarUrl,
            'messageCreated': messageCreated,
            'roomId': roomId,
        }))
    

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_id,
            self.channel_name,
        )
    
    @sync_to_async
    def save_message(self, messageUser, room, message):
        user = User.objects.get(name=messageUser)
        room = Room.objects.get(id=room)

        Messages.objects.create(user=user, room=room, body=message)