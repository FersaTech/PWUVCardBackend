from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import CartDataModel, User

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    search_fields = ['first_name','email', 'last_name', 'mobile','area_pin']
    list_display = ['email', 'first_name', 'last_name', 'mobile', 'admin']
    list_filter = ['admin']
    fieldsets = (
        ('Basic Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'mobile', 'address', 'area_pin', 'profile_picture')}),
        ('Permissions', {'classes':('collapse',),'fields': ('admin', 'staff', 'is_active',  'is_merchant')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'mobile', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email', 'first_name', 'last_name', 'mobile', 'id']
    ordering = ['email']
    filter_horizontal = ()

# admin.site.unregister(User)

admin.site.register(User, UserAdmin)


admin.site.register(CartDataModel)