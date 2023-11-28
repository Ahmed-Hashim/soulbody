import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import PublishedPost


@receiver(post_save, sender=PublishedPost)
def send_notification_on_signal(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        group_name = 'user-notifications'
        data = {
            'id': instance.id,
            'thumbnail': instance.link,
            'message': instance.message,
            'category': instance.category.name,
            'scheduled_by': instance.scheduled_by.profile.fullname,
            'published_date': instance.published_date,
            'fblink': instance.fblink
        }
        my_json_str = json.dumps(data)
        event = {
            'type': 'published_post',
            'text': my_json_str
        }
        try:
            async_to_sync(channel_layer.group_send)(
                group_name, event
            )
        except Exception as e:
            # Handle exceptions here
            print(f"Error sending notification: {str(e)}")
