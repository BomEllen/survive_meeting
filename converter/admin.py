from django.contrib import admin
from .models import ConversionTemplate, ConversionLog


@admin.register(ConversionLog)
class ConversionLogAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'tone', 'input_text', 'result_1']
    list_filter = ['tone', 'created_at']
    search_fields = ['input_text']
    readonly_fields = ['input_text', 'tone', 'result_1', 'result_2', 'result_3', 'created_at']
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(ConversionTemplate)
class ConversionTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'tone', 'keywords', 'is_active', 'updated_at']
    list_filter = ['tone', 'is_active']
    search_fields = ['name', 'keywords']
    list_editable = ['is_active']
    fieldsets = (
        ('기본 정보', {
            'fields': ('name', 'keywords', 'tone', 'is_active')
        }),
        ('변환 결과 문장', {
            'fields': ('result_1', 'result_2', 'result_3'),
            'description': '최소 1개, 최대 3개의 변환 결과 문장을 입력하세요.'
        }),
    )

admin.site.site_header = '🏢 회의에서 살아남기 관리자'
admin.site.site_title = '회의에서 살아남기'
admin.site.index_title = '변환 템플릿 관리'
