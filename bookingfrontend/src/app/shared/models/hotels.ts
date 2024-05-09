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
}

export interface Amenity {
  name: string
  image: string
}

export interface Service {
  title: string;
  description: string;
  image: string;
}
