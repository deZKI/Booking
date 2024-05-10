export interface Hotel {
  id: number;
  price: number;
  name: string;
  location: string;
  description: string
  rating: number;
  image: string;
}

export interface HotelDetail extends Hotel {
  amenities: Amenity[]
  rooms: Room[]
}

export interface Amenity {
  name: string
  image: string
}

export interface Room {
  id: number
  room_number: number
  room_type_display: string
  images: Image[]
}

export interface RoomDetail extends Room {
  price: number
  amenities: Amenity[]
  hotel: Hotel
}

export interface Service {
  title: string;
  description: string;
  image: string;
}

export interface Image {
  image: string
}

export interface BookingCreation {
  room: Room | number;
  check_in: Date,
  check_out: Date,
  guest_surname: string,
  guest_name: string,
  guest_number: string,
  guest_email: string
}


export interface Booking extends BookingCreation {
  id: number;
  price: number;
  status: string;
  user: number
}
