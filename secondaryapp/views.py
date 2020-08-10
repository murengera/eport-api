from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins,generics
from .serializer import *
from .models import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import SearchFilter
from .pagination  import LargeResultsSetPagination
from django.contrib.auth.models import Group




class CategoryList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    name='category-list'

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):

        user=request.user
        user_group = user.groups.first()
        staff=Group.objects.get(name='NexinStaff')
        if user_group == staff and user.is_staff:
          return self.create(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation "}, status=403)




class CategoryDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes = [IsAdminUser,IsAuthenticated]
    lookup_field='name'
    name='category-detail'
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args)

    def update(self,request,*args,**Kwargs):
        return self.update(request,*args,**Kwargs)

    def destroy(self,request,*args,**Kwargs):
        return self.destroy(request,*args,**Kwargs)



class SecondaryList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class=SecondarySerializer
    queryset=Secondary.objects.all().order_by('name')

    pagination_class = LargeResultsSetPagination
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['name',]
    name='secondary-list'


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        user=request.user
        user_group = user.groups.first()
        staff=Group.objects.get(name='NexinStaff')
        if user_group == staff and user.is_staff:
          return self.create(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation "}, status=403)



class SecondaryDetail(mixins.RetrieveModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class=SecondarySerializer
    queryset=Secondary.objects.all()
    lookup_field='name'
    permission_classes=[IsAuthenticated,IsAdminUser]
    name='secondary-detail'

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args)


    def update(self,request,*args,**Kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='NexinStaff')
        staffschool=Group.objects.get(name='SchoolStaff')
        if user_group == staff  or user_group== staffschool:
            return self.partial_update(request, *args, **kwargs)
        return Response({"detail": "either schoolstaff or nexinstff is  allowed to perform such operation   "}, status=403)

    def delete(self,request,*args,**Kwargs):
        user=request.user
        user_group = user.groups.first()
        staff=Group.objects.get(name='NexinStaff')
        if user_group == staff and user.is_staff:
          return self.destroy(request,*args,**Kwargs)
        return Response({"detail": "only our Nexin Staff can delete a school"}, status=403)






    """
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter,)
	filter_fields = "__all__"



    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    filter_backends = [DjangoFilterBackend]
    filters_fields = ['name']

    filters
    pagination


    """

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
           'secondary-categories': reverse(CategoryList.name, request=request),
           'secondary-list': reverse(SecondaryList.name, request=request),


})

