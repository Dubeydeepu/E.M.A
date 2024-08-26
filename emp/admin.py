from django.contrib import admin
from .models import Emp,Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    search_fields=('name',)

#REGISTER YOUR MODELS HERE

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
