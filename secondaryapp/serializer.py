from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secondary
        fields = '__all__'

        def to_representation(self,instance):
            serializer_data=super(SecondarySerializer,self).to_representation(instance)
            serializer_data['Category']=CategorySerializer(instance.Category).data
            return serializer_data





        """
        def validate_name(self, value):
            qs=Category.objects.filter(name=value)
            if qs.exists():
                raise serializers.ValidationError(" that category is already added :no duplication is allowed")
                return value

"""