from django.contrib import admin
# from courses.admin import ModuleInline
from .models import Theme, Clas


@admin.register(Theme)
class ThemesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Clas)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'themes', 'created']
    list_filter = ['created', 'themes']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [ModuleInline]
