from django.contrib import admin
from django.urls import path,include
from api.views  import CompanyViewSet,EmployessViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employess',EmployessViewSet)

urlpatterns = [
 path('',include(router.urls))
 
]