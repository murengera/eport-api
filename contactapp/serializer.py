from rest_framework import serializers
from contactapp.models import Subscribe,ContactForm



class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscribe
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactForm
        fields='__all__'

    