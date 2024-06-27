from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.urls import reverse_lazy
from django.views.generic import CreateView

from notify.forms import CarForm
from notify.models import Notification


def send_notification_view(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'send_notification',
            'message': 'Esta é uma notificação de teste!'
        }
    )
    return render(request, 'index.html')


class NotificationCreateView(CreateView):
    model = Notification
    form_class = CarForm
    template_name = 'new_notification.html'
    success_url = reverse_lazy('sucess')


def sucess(request):
    return render(request, 'sucess.html')
