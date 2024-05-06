from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User


class Hotel(models.Model):
    """Модель для представления отеля."""
    name = models.CharField(max_length=200, verbose_name="Название")
    location = models.CharField(max_length=300, verbose_name="Местоположение")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Превью отеля", blank=True)
    rating = models.PositiveIntegerField(verbose_name="Количество звезд",
                                         validators=[MinValueValidator(0), MaxValueValidator(5)])

    @property
    def price(self):
        min_price = self.room_set.aggregate(models.Min('price'))['price__min']
        return min_price if min_price is not None else 0

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return self.name


class Amenity(models.Model):
    """Модель для представления удобств, доступных в отеле или номере."""
    name = models.CharField(max_length=100, verbose_name="Название удобства")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Удобство'
        verbose_name_plural = 'Удобства'


class Room(models.Model):
    """Модель для представления номера в отеле."""

    class RoomType(models.TextChoices):
        SINGLE = 'single', 'Одноместный'
        DOUBLE = 'double', 'Двухместный'
        SUITE = 'suite', 'Люкс'
        FAMILY = 'family', 'Семейный'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    room_number = models.CharField(max_length=10, verbose_name="Номер комнаты")
    room_type = models.CharField(
        max_length=20,
        choices=RoomType.choices,
        default=RoomType.SINGLE,
        verbose_name="Тип комнаты"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена за ночь")
    amenities = models.ManyToManyField(Amenity, verbose_name="Удобства")

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return f'{self.hotel}: {self.room_type}'


class Booking(models.Model):
    """Модель для представления бронирования номера."""

    class BookingStatus(models.TextChoices):
        CONFIRMED = 'confirmed', 'Подтверждено'
        CANCELLED = 'cancelled', 'Отменено'
        PENDING = 'pending', 'В ожидании'
        CHECKED_IN = 'checked_in', 'Заселён'
        CHECKED_OUT = 'checked_out', 'Выселен'

    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Забронированный номер")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    check_in = models.DateField(verbose_name="Дата заезда")
    check_out = models.DateField(verbose_name="Дата выезда")
    guests = models.IntegerField(verbose_name="Количество гостей")
    status = models.CharField(
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING,
        verbose_name="Статус бронирования"
    )

    def __str__(self):
        return f'{self.room}: {self.status}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

    def clean(self):
        """Проверка, не перекрываются ли даты нового бронирования с уже существующими бронированиями."""
        super().clean()
        bookings = Booking.objects.filter(room=self.room).exclude(id=self.id)
        for booking in bookings:
            if booking.check_out > self.check_in and booking.check_in < self.check_out:
                raise ValidationError("Даты бронирования перекрываются с существующим бронированием.")

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.clean()
        super(Booking, self).save(force_insert, force_update, using, update_fields)  # Вызов оригинального метода save


class HotelImage(models.Model):
    """Модель для представления изображений отеля."""
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE, verbose_name="Отель")
    image = models.ImageField(upload_to='hotel_images/', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Изображение отеля'
        verbose_name_plural = 'Изображения отелей'


class RoomImage(models.Model):
    """Модель для представления изображений номера."""
    room = models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE, verbose_name="Номер")
    image = models.ImageField(upload_to='room_images/', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Изображение номера'
        verbose_name_plural = 'Изображения номеров'
