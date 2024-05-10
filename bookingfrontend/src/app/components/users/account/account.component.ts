import {Component, OnInit} from '@angular/core';
import {BookingService} from "../../../services/booking.service";
import {Booking} from "../../../shared/models/hotels";
import {take, tap} from "rxjs";
import {AuthService} from "../../../services/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrl: './account.component.scss'
})
export class AccountComponent implements OnInit {
  bookings: Booking[] = [];

  constructor(private bookingService: BookingService,
              private authService: AuthService,
              private router: Router
  ) {
  }

  ngOnInit() {
    this.loadUserBookings();
  }

  loadUserBookings() {
    this.bookingService.getBookings().pipe(
      take(1),
      tap(bookings => this.bookings = bookings)
    ).subscribe();
  }

  logout() {
    this.authService.logout()
    this.router.navigate([''])
  }
}
