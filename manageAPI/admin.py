from django.contrib import admin
from manageAPI.models import User, Business, Products
from django.contrib.auth.admin import UserAdmin


# Register your models here.

@admin.register(User)
class userAdmins(UserAdmin):
    """
    manage user view on admin pannel
    """
    list_display = ['email', 'username', 'name', 'bio', 'is_active', 'is_admin', 'is_staff']
    search_fields = ['email', 'username']
    readonly_fields = ['joined_date', 'last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Business)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ['registrationNo', 'email', 'name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'mrp', 'description', 'user', 'business']
