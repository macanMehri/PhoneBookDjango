from django.contrib import admin
from .models import Address, Person
import csv
from django.http import HttpResponse


# Add new actions

@admin.action(description='Activate selected items')
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='Download selected items as csv')
def download_csv_person(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="people.csv"'
        writer = csv.writer(response)
        writer.writerow([
             'id',
             'first_name',
             'last_name',
             'number',
             'address'
        ])
        data = Person.objects.filter()
        for row in data:
            rowobj = [
                 row.id,
                 row.first_name,
                 row.last_name,
                 row.number,
                 row.address,
            ]
            
            writer.writerow(rowobj)

        return response


@admin.action(description='Download selected items as csv')
def download_csv_address(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="addresses.csv"'
        writer = csv.writer(response)
        writer.writerow([
             'id',
             'country',
             'city',
             'exact_location',
        ])
        data = Address.objects.filter()
        for row in data:
            rowobj = [
                 row.id,
                 row.country,
                 row.city,
                 row.exact_location,
            ]
            
            writer.writerow(rowobj)

        return response


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
        download_csv_address,
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
        download_csv_person,
    )
