from django.contrib import admin

from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Admin interface for managing Todo items."""
    list_display = ('title', 'user', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    
    def get_queryset(self, request):
        """Limit queryset to the todos of the logged-in user."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

