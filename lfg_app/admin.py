from django.contrib import admin
from .models import Proposal

# Register your models here.
class Filter(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_filter = ('status',)

admin.site.register(Proposal, Filter)