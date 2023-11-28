import json
from channels.generic.websocket import WebsocketConsumer ,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template
from members.models import Chat, Messege, Profile, ChatNotification
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.GROUP_NAME = 'user-notifications'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def published_post(self, event):
        data = json.loads(event["text"])

        id = data['id']
        thumbnail = data['thumbnail']
        message = data['message']
        category = data['category']
        scheduled_by = data['scheduled_by']
        published_date = data['published_date']
        fblink = data['fblink']
        html = get_template("notification/noti.html").render(
            context={
                'id': id,
                'thumbnail': thumbnail,
                'message': message,
                'category': category,
                'scheduled_by': scheduled_by,
                'published_date': published_date,
                'fblink': fblink
            })
        self.send(text_data=html)

    def send_toast(self, event):
        data = (event["text"])
        self.send(text_data=data)
class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']

        await self.save_message( message,receiver)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_message(self, message,receiver):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(other_user_id) > int(my_id):
            chat_model = Chat.objects.filter(
                user1=other_user_id, user2=my_id).first()
        else:
            chat_model = Chat.objects.filter(
                user1=my_id, user2=other_user_id).first()
        chat_obj = Messege.objects.create(
            sender=User.objects.get(id=self.scope['user'].id), content=message, chat=chat_model)
        get_user = User.objects.get(id=other_user_id)
        if receiver == get_user.username:
            ChatNotification.objects.create(chat=chat_obj, user=get_user)
class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'user'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        username = data['username']
        connection_type = data['type']
        await self.change_online_status(username, connection_type)

    async def send_onlineStatus(self, event):
        data = json.loads(event.get('value'))
        username = data['username']
        online_status = data['status']
        await self.send(text_data=json.dumps({
            'username':username,
            'online_status':online_status
        }))

    async def disconnect(self, message):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def change_online_status(self, username, c_type):
        user = User.objects.get(username=username)
        userprofile = Profile.objects.get(user=user)
        if c_type == 'open':
            userprofile.online_status = True
            userprofile.save()
        else:
            userprofile.online_status = False
            userprofile.save()