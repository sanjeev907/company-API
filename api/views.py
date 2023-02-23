from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets 
from api.models import Company,Employess
from api.serializers import CompanySerializer
from api.serializers import EmployessSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# create views here

class CompanyViewSet(viewsets.ModelViewSet):

    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    

# companies/{companyId}/employess
    @action(detail=True,methods=['get'])
    def employess(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employess.objects.filter(Company=company)
            emp_serializer=EmployessSerializer(emps,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return ResourceWarning({
                'message':e
            })

class EmployessViewSet(viewsets.ModelViewSet):
    queryset=Employess.objects.all()
    serializer_class=EmployessSerializer