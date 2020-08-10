from django.contrib.auth import authenticate
from rest_framework import exceptions
from rest_framework import serializers
from .models import  *
from django.contrib.auth import get_user_model


class FacultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facult
        fields=('id','name','fees','course','programoffer',)

    def to_representation(self, instance):
            serialized_data = super(FacultSerializer, self).to_representation(instance)
            #serialized_data['programoffer'] = ProgramSerializer(instance.programoffer).data
            #serialized_data['university'] = UniverstiesSerializer(instance.university).data

            return serialized_data






class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model=Program
        fields=('id','program','duration','university')

    def to_representation(self, obj):
            serialized_data = super(ProgramSerializer,self).to_representation(obj)
            serialized_data['university'] = UniverstiesSerializer(obj.university).data


            return serialized_data;








class DepartmentSerializer(serializers.ModelSerializer):

            class Meta:
                model = Department
                fields = ('id','name','head_department','contacts','email','facult')

            def to_representation(self, instance):
                serialized_data = super(DepartmentSerializer, self).to_representation(instance)
                serialized_data['facult'] = FacultSerializer(instance.facult).data
                return serialized_data







class UniverstiesSerializer(serializers.ModelSerializer):



    class Meta:
        model=University
        fields=('__all__')





class UniverstiesSerializerdetail(serializers.ModelSerializer): 
    programs=ProgramSerializer(many=True,read_only=True)
    facults=FacultSerializer(many=True,read_only=True)
    departments=DepartmentSerializer(many=True,read_only=True)
    created_at = serializers.DateField(format=None, input_formats=None)



    class Meta:
        model = University
        fields=['name','description','email','phone','website','province','district','sector','more_info','log','ownershipstatus','programs','facults','departments',]


