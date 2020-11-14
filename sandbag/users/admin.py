from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User,Token

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username','is_staff','token' ,'is_superuser']
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','token')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff','is_superuser', 'is_active','token')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class CustomUserToken(admin.ModelAdmin):
    model = Token
    list_display = ['token','is_valid','username']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Token,CustomUserToken)