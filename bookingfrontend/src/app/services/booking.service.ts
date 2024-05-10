import {Injectable} from '@angular/core';
import {environment} from "../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Booking, BookingCreation} from "../shared/models/hotels";

@Injectable({
  providedIn: 'root'
})
export class BookingService {

  private apiBooking = `${environment.apiUrl}/bookings/`

  constructor(private http: HttpClient) {
  }

  getBookings(): Observable<Booking[]> {
    return this.http.get<Booking[]>(this.apiBooking);
  }

  createBooking(booking: BookingCreation): Observable<BookingCreation> {
    return this.http.post<BookingCreation>(this.apiBooking, booking)
  }
}
