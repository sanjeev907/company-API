from rest_framework import serializers
from api.models import Company,Employess



# create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class EmployessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employess
        fields="__all__"