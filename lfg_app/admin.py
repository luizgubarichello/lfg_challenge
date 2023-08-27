from django.contrib import admin
from .models import ProposalField, ProposalFieldValue, Proposal


class ProposalFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'type', 'required')
    list_filter = ('type', 'required')
    search_fields = ('name', 'label')


class ProposalFieldValueAdmin(admin.ModelAdmin):
    list_display = ('field', 'value')
    list_filter = ('field',)
    search_fields = ('value',)


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('fields',)


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalField, ProposalFieldAdmin)
admin.site.register(ProposalFieldValue, ProposalFieldValueAdmin)