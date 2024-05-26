
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.utils.html import format_html


class ProfileAdmin(UserAdmin):
    list_display = ('thumbnail','user_name', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_admin','is_staff', 'is_active','is_inactive')
    list_display_links = ('thumbnail','user_name', 'email',)
    readonly_fields = ('first_name', 'last_name', 'last_login', 'date_joined',) # 'is_admin','is_staff', 'is_active','is_inactive'?
    ordering = ('-date_joined',)

    # Added due to custom class
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def thumbnail(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(obj.profile_picture.url))
        else:
            return None

    thumbnail.short_description = 'Profile Picture'


admin.site.register(Profile, ProfileAdmin)

