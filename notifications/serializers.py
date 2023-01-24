from rest_framework import serializers
from . import models

class SendedNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = ('type', 'subtitle','user','item','related_user')
