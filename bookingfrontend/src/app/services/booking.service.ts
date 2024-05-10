import {Injectable} from '@angular/core';
import {environment} from "../../environments/environment";
import {HttpClient, HttpParams} from "@angular/common/http";
import {Observable} from "rxjs";
import {Booking, BookingCreation, BookingDates} from "../shared/models/hotels";

@Injectable({
  providedIn: 'root'
})
export class BookingService {

  private apiBooking = `${environment.apiUrl}/bookings/`
  private apiBookingDates = this.apiBooking + 'booking-dates-by-room/'

  constructor(private http: HttpClient) {
  }

  getBookings(): Observable<Booking[]> {
    return this.http.get<Booking[]>(this.apiBooking);
  }

  getBookingsDates(roomId: number): Observable<BookingDates[]> {
    const params = new HttpParams().set('room_id', roomId.toString());
    return this.http.get<BookingDates[]>(this.apiBookingDates,  { params });
  }

  createBooking(booking: BookingCreation): Observable<BookingCreation> {
    return this.http.post<BookingCreation>(this.apiBooking, booking)
  }
}
