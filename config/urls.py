from django.contrib import admin
from django.urls import path

from notify.views import send_notification_view, sucess, NotificationCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sucess/', sucess, name='sucess'),
    path('create/', NotificationCreateView.as_view(), name='create'),
    path('', send_notification_view, name='send_notification'),
]
