from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Skill

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')

    def save_model(self, request, obj, form, change):
        obj.save()

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name',)
