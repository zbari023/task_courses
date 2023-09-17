from django.contrib import admin

from .models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_filter = ['name','price']
    search_fields = ['name','price']
    
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Review)
admin.site.register(Category)