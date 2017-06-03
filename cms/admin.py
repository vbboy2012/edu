from django.contrib import admin
from .models import Menu,Role

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','parent_id','url','type','status','name','icon','remark','order')


admin.site.register(Menu,MenuAdmin)
admin.site.register(Role)
