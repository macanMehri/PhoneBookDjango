from django.contrib import admin
from .models import Address, Person


# Add new actions

@admin.action(description='Activate selected items')
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'country',
        'city',
        'exact_location',
        'is_active',
        'created_date',
        'updated_date',
    )

    list_display_links = ('id', 'country', 'city')
    list_filter = ('is_active', 'created_date', 'updated_date')
    search_fields = ('id', 'title', 'description')
    # Order by primary key
    ordering = ('pk',)

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'first_name',
        'last_name',
        'number',
        'address',
        'is_active',
        'created_date',
        'updated_date',
    )

    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('is_active', 'created_date', 'updated_date')
    search_fields = ('id', 'title', 'description')
    # Order by primary key
    ordering = ('pk',)

    actions = (
        activate_selected_items,
        deactivate_selected_items,
    )
