import factory
from faker import Faker
from .models import Hotel, Room, Amenity, Booking, HotelImage, RoomImage
from django.contrib.auth.models import User

fake = Faker()


class HotelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hotel

    name = factory.LazyAttribute(lambda _: fake.company())
    location = factory.LazyAttribute(lambda _: fake.address())
    description = factory.LazyAttribute(lambda _: fake.text())


class AmenityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Amenity

    name = factory.LazyAttribute(lambda _: fake.word())


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    hotel = factory.SubFactory(HotelFactory)
    room_number = factory.Sequence(lambda n: f"{100 + n}")
    room_type = factory.Iterator([choice[0] for choice in Room.RoomType.choices])
    price = factory.LazyAttribute(lambda _: fake.random_number(digits=3))
    amenities = factory.RelatedFactoryList(AmenityFactory, 'room', size=3)


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    room = factory.SubFactory(RoomFactory)
    user = factory.SubFactory(factory.django.DjangoModelFactory, model=User)
    check_in = factory.LazyAttribute(lambda _: fake.date_this_year())
    check_out = factory.LazyAttribute(lambda _: fake.date_this_year())
    guests = factory.LazyAttribute(lambda _: fake.random_int(min=1, max=4))
    status = factory.Iterator([choice[0] for choice in Booking.BookingStatus.choices])


class HotelImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HotelImage

    hotel = factory.SubFactory(HotelFactory)
    image = factory.django.ImageField()


class RoomImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoomImage

    room = factory.SubFactory(RoomFactory)
    image = factory.django.ImageField()
