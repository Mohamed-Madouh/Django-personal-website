from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class postSomeModelAdmin (SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'














admin.site.register( post , postSomeModelAdmin )