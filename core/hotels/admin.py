from django.contrib import admin
from django.utils.html import format_html
from .models import Hotel, Room, Booking, Amenity, HotelImage, RoomImage, Service

from image_uploader_widget.admin import ImageUploaderInline


class HotelImageAdmin(ImageUploaderInline):
    """Использование сторонней библиотеки для
        добавления нескольких фотографий за раз"""
    model = HotelImage


class RoomImageAdmin(ImageUploaderInline):
    """Использование сторонней библиотеки для
        добавления нескольких фотографий за раз"""
    model = RoomImage


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description', 'image_preview',)  # Отображаемые поля в списке
    search_fields = ('name', 'location')  # Поля, по которым можно осуществлять поиск

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Превью'

    inlines = [
        HotelImageAdmin,
    ]


class AmenityAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Поля для поиска


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'hotel', 'price')  # Отображаемые поля
    list_filter = ('room_type', 'hotel')  # Фильтры для удобства навигации
    search_fields = ('room_number', 'hotel__name')  # Поиск по номеру и отелю

    inlines = [
        RoomImageAdmin,
    ]


class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in', 'check_out', 'status')  # Отображаемые поля
    list_filter = ('status', 'check_in', 'check_out')  # Фильтры
    search_fields = ('user__username', 'room__room_number', 'status')  # Поиск по полям


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', )


# Регистрация моделей и их админ-классов
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Service, ServiceAdmin)
