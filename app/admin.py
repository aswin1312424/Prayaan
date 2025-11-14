from django.contrib import admin
from .models import Car, Booking, Maintenance, Driver, Customer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['category', 'ac_type', 'registration_number', 'total_cars', 'price', 'status']
    list_filter = ['ac_type', 'status', 'fuel_consumption']
    search_fields = ['category', 'registration_number']
    readonly_fields = ['created_at'] if hasattr(Car, 'created_at') else []
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'ac_type', 'registration_number', 'fuel_consumption')
        }),
        ('Pricing', {
            'fields': ('price', 'price_per_hour', 'price_per_km')
        }),
        ('Inventory', {
            'fields': ('total_cars', 'status')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Return Information', {
            'fields': ('is_returned', 'returned_at', 'pending_payment', 'damage_reported', 'damage_fee')
        }),
    )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'license_number', 'aadhar_number', 'status', 'experience']
    list_filter = ['status', 'experience']
    search_fields = ['name', 'phone', 'license_number', 'aadhar_number']
    readonly_fields = ['created_at'] if hasattr(Driver, 'created_at') else []


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'aadhar_number', 'license_number']
    search_fields = ['user__username', 'phone', 'aadhar_number']
    readonly_fields = ['user']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'car', 'start_datetime', 'is_returned', 'total_amount', 'pending_payment']
    list_filter = ['is_returned', 'start_datetime', 'drive_type']
    search_fields = ['customer__username', 'car__category']
    readonly_fields = ['created_at', 'returned_at']
    fieldsets = (
        ('Booking Details', {
            'fields': ('customer', 'car', 'drive_type')
        }),
        ('DateTime', {
            'fields': ('start_datetime', 'expected_return_datetime', 'actual_return_datetime', 'returned_at', 'created_at')
        }),
        ('Location & Distance', {
            'fields': ('pickup_location', 'drop_location', 'distance_km', 'kms_to_destination', 'hours_used')
        }),
        ('Payment', {
            'fields': ('total_amount', 'advance_payment', 'pending_payment')
        }),
        ('KM Reading', {
            'fields': ('start_km_reading', 'end_km_reading')
        }),
        ('Damage & Return', {
            'fields': ('damage_reported', 'damage_fee', 'is_returned')
        }),
        ('Other', {
            'fields': ('night_halt',)
        }),
    )


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'cost']
    list_filter = ['date', 'car']
    search_fields = ['car__category', 'car__registration_number']
    readonly_fields = ['created_at'] if hasattr(Maintenance, 'created_at') else []

