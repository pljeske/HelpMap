from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from social.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializes a Message object to its JSON representation (used in REST API).
    """
    sender = StringRelatedField(many=False)
    receiver = StringRelatedField(many=False)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'text', 'date']
