from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from notify.models import Notification

import uuid


@receiver(post_save, sender=Notification)
def notification_post_save(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'send_notification',
            'message': f'Notification sent successfully = {uuid.uuid4()}',
        }
    )
    print('Notification sent successfully')
