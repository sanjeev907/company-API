from django.contrib import admin
from api.models import Company,Employess
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','type','location')
    search_fields=('name',)

class EmployessAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone')
    list_filter=('name',)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employess,EmployessAdmin)