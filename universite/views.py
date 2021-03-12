from rest_framework.filters import SearchFilter
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from .pagination import PostPageNUmberPagination
from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.response import Response
from accounts.permission import *
from django_filters import FilterSet
from django_filters import rest_framework as filters
from  rest_framework.filters import  OrderingFilter







class UniversityFilter(FilterSet):

    name=filters.CharFilter(method="filter_by_name")
    province=filters.CharFilter(method="filter_by_province")
    class Meta:
        model=University
        fields=('name','province')

    def filter_by_name(self,queryset,name,value):
        queryset=queryset.filter(name__contains=value)
        return  queryset

    def filter_by_province(self, queryset, name, value):
        queryset = queryset.filter(province__contains=value)
        return queryset


#university list








class UniversityLists(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    serializer_class = UniverstiesSerializer
    queryset = University.objects.all().order_by('name')
    pagination_class = PostPageNUmberPagination
    permission_classes = [IsOwnerOrReadOnly,]

    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filter_class=UniversityFilter
    filter_fields =('__all__')
    search_fields=['name',]
    ordering_fields=('name')



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):


        user=request.user
        user_group = user.groups.first()
        staff=Group.objects.get(name='Staffs')
        if user_group == staff and user.is_staff:
          return self.create(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except  system administrator  "},status=403)




#university detail
class UniversityDetail(generics.GenericAPIView,
                             mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = UniverstiesSerializerdetail
    queryset = University.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]



    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool=Group.objects.get(name='SchoolStaffs')
        if user_group == staff  or user_group== staffschool :
            return self.partial_update(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except  university staff and system administrator "}, status=403)


    def delete(self, request, *args, **kwargs):

       user = request.user
       user_group = user.groups.first()
       staff = Group.objects.get(name='Staffs')
       staffschool=Group.objects.get(name='SchoolStaffs')
       if user_group==staff or user_group== staffschool or user.is_active:
         return self.destroy(request, *args, **kwargs)
       return Response({"detail": "You are not allowed to perform such operation except  system administrator "}, status=403)


#program list
class ProgramList(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
        serializer_class = ProgramSerializer
        queryset = Program.objects.all()
        filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
        pagination_class = PostPageNUmberPagination

        filter_fields = ('__all__')
        search_fields = ('program','university__id','university__name','university__province','university__district','university__sector','university__sector',)
        ordering_fields = ('university__name', )

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            user = request.user
            user_group = user.groups.first()
            staffschool = Group.objects.get(name='SchoolStaffs')
            staff = Group.objects.get(name='Staffs')
            if user_group == staff or user_group==staffschool:
             return self.create(request, *args, **kwargs)
            return Response({"detail": "You are not allowed to perform such operation except  university staff and  system administrator "}, status=403)



#program detail
class ProgramDetail(generics.GenericAPIView,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool=Group.objects.get(name='SchoolStaffs')
        if user_group == staff  or user_group== staffschool:
            return self.partial_update(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except  university staff and system administrator "}, status=403)


    def delete(self, request, *args, **kwargs):

        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool = Group.objects.get(name='SchoolStaffs')
        if user_group == staff or user_group==staffschool:
            return self.destroy(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except university staff and  system administrator   "}, status=403)




#department list
class DepartmentList(generics.GenericAPIView,
                               mixins.ListModelMixin,
                               mixins.CreateModelMixin):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    pagination_class = PostPageNUmberPagination

    filter_fields = ('name',)
    search_fields = ('name','university__id','university__name','university__province','university__district',)
    ordering_fields = ('university__created_at',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staffschool = Group.objects.get(name='SchoolStaffs')
        staff = Group.objects.get(name='Staffs')
        if user_group == staff or user_group==staffschool:
            return self.create(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except  university staff and  system administrator "}, status=403)


#department detail
class DepartmentDetail(generics.GenericAPIView,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = DepartmentSerializer

    queryset = Department.objects.all()
    permission_classes = [IsOwnerOrReadOnly, ]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool=Group.objects.get(name='SchoolStaffs')
        if user_group == staff  or user_group== staffschool:
          return self.partial_update(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except   staff form university and system administrator   "}, status=403)


    def delete(self, request, *args, **kwargs):

        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool = Group.objects.get(name='SchoolStaffs')
        if user_group == staff or user_group == staffschool:
            return self.destroy(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except   system administrator "}, status=403)

#facult list
class FacultLIst(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    serializer_class = FacultSerializer
    queryset = Facult.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    pagination_class = PostPageNUmberPagination

    filter_fields = ('name',)
    search_fields = ('program', 'university__id', 'university__province', 'university__district', 'university__sector',)
    ordering_fields = ('name',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool = Group.objects.get(name='SchoolStaffs')
        if user_group == staff or user_group==staffschool:
            return self.create(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except   system administrator "}, status=403)


#facult detail
class FacultDetail(generics.GenericAPIView,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = FacultSerializer

    queryset = Facult.objects.all()


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        user = request.user
        user_group = user.groups.first()
        staff = Group.objects.get(name='Staffs')
        staffschool=Group.objects.get(name='SchoolStaffs')
        if user_group == staff  or user_group== staffschool:
            return self.partial_update(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except    university staff and system administrator   "}, status=403)


    def delete(self, request, *args, **kwargs):

        user = request.user
        user_group = user.groups.first()

        
        staff = Group.objects.get(name='Staffs')
        staffschool = Group.objects.get(name='SchoolStaffs')
        if user_group == staff or user_group == staffschool:
            return self.destroy(request, *args, **kwargs)
        return Response({"detail": "You are not allowed to perform such operation except university staff and system administrator "}, status=403)
