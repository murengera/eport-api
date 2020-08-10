from django.shortcuts import render
from rest_framework import generics,viewsets
from django_filters import rest_framework as filters
from .serializer import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticated,IsAdminUser
from .models import *


class Subscribers(generics.RetrieveUpdateDestroyAPIView):
    queryset=Subscribe.objects.all()
    serializer_class=SubscribeSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]
    name='subscribe'
    lookup_field=['name']
    
    def get_subscribe_data(self):
        return  queryset
class Contacts(generics.RetrieveUpdateDestroyAPIView):
    queryset=ContactForm.objects.all()
    serializer_class=ContactSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]
    lookup_field=['name']
    name='contacts'

    def get_contacts_data(self):
        return queryset
        
    """

class Api(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
           'registration': reverse(UserCategoryList.name, request=request),
           'subscribers': reverse(Subscribers.name, request=request),
           'contacts': reverse(Contacts.name, request=request),
         

})
"""