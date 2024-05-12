import {Component, OnInit} from '@angular/core';
import {BookingCreation, BookingDates, RoomDetail} from "../../../shared/models/hotels";
import {HotelsService} from "../../../services/hotels.service";
import {ActivatedRoute} from "@angular/router";
import {of, take, tap} from "rxjs";
import {AbstractControl, FormBuilder, FormGroup, ValidatorFn, Validators} from "@angular/forms";
import {BookingService} from "../../../services/booking.service";
import {addDays, differenceInCalendarDays, format} from 'date-fns';
import {catchError} from "rxjs/operators";

@Component({
  selector: 'app-room-detail',
  templateUrl: './room-detail.component.html',
  styleUrl: './room-detail.component.scss'
})
export class RoomDetailComponent implements OnInit {
  room!: RoomDetail;
  hotelId!: number;
  roomId!: number;
  bookingForm!: FormGroup;
  totalCost: number = 0
  nightsCount: number = 0
  bookedDates: Date[] = [];
  minDate = new Date(); // Текущая дата
  constructor(
    private hotelService: HotelsService,
    private bookingService: BookingService,
    private route: ActivatedRoute,
    private fb: FormBuilder,
  ) {
  }

  ngOnInit() {
    this.hotelId = this.route.snapshot.params['hotelId']
    this.roomId = this.route.snapshot.params['roomId']
    this.hotelService.getRoomById(this.roomId).pipe(
      take(1),
      tap(room => {
        this.room = room
      })
    ).subscribe()
    this.bookingService.getBookingsDates(this.roomId).pipe(
      take(1),
      tap(bookings => {
        this.bookedDates = this.flattenBookings(bookings);
      })
    ).subscribe()
    this.initForm();
  }

  initForm() {
    this.bookingForm = this.fb.group({
      surname: ['', Validators.required],
      name: ['', Validators.required],
      email: ['', [Validators.required]],
      phone: ['', [Validators.required]],
      arrivalDate: ['', Validators.required],
      departureDate: ['', Validators.required]
    }, {validator: this.dateRangeValidator});
    this.bookingForm.get('arrivalDate')!.valueChanges.subscribe(_ => this.calculateTotal());
    this.bookingForm.get('departureDate')!.valueChanges.subscribe(_ => this.calculateTotal());

  }

  bookRoom() {
    if (this.bookingForm.valid) {
      const bookingData: BookingCreation = {
        room: this.roomId,
        check_in:  format(this.bookingForm.get('arrivalDate')?.value, 'yyyy-MM-dd'),
        check_out: format(this.bookingForm.get('departureDate')?.value, 'yyyy-MM-dd'),
        guest_surname: this.bookingForm.get('surname')?.value,
        guest_name: this.bookingForm.get('name')?.value,
        guest_number: this.bookingForm.get('phone')?.value,
        guest_email: this.bookingForm.get('email')?.value
      };
      this.bookingService.createBooking(bookingData).pipe(
        take(1),
        tap(response => {
          alert('Номер успешно забронирован. С вами свяжутся.')
        }),
        catchError(error => {
          alert('Ошибка. ' + error)
          return of(null); // Возвращаем Observable, который выпускает `null`, это предотвращает "краш" потока.
        })
      ).subscribe()
    }
  }

  getStars(rating: number): any[] {
    return new Array(rating);
  }

  private dateRangeValidator: ValidatorFn = (group: AbstractControl): {[key: string]: any} | null => {
    const start = group.get('arrivalDate')?.value;
    const end = group.get('departureDate')?.value;
    if (!start || !end) {
      return null;  // Если даты не выбраны, валидатор не применяется
    }

    let currentDate = new Date(start);
    const endDate = new Date(end);

    while (currentDate <= endDate) {
      if (this.isDateBooked(currentDate)) {
        return { 'dateRangeInvalid': 'В диапозоне есть заблокированная дата: ' + format(currentDate, 'yyyy-MM-dd') };  // Возвращает ошибку, если находит забронированную дату
      }
      currentDate = addDays(currentDate, 1);
    }

    return null;  // Все дни в диапазоне доступны
  }


  private calculateTotal() {
    const arrivalDate = new Date(this.bookingForm.get('arrivalDate')!.value);
    const departureDate = new Date(this.bookingForm.get('departureDate')!.value);

    if (isNaN(arrivalDate.getTime()) || isNaN(departureDate.getTime())) {
      return;
    }

    this.nightsCount = differenceInCalendarDays(departureDate, arrivalDate);

    if (this.nightsCount > 0) {
      this.totalCost = this.nightsCount * this.room.price;
    } else {
      this.totalCost = 0;
    }
  }

  private flattenBookings(bookings: BookingDates[]): Date[] {
    const dates: Date[] = [];
    bookings.forEach(booking => {
      const start = new Date(booking.check_in);
      const end = new Date(booking.check_out);
      let current = start;
      while (current <= end) {
        dates.push(new Date(current));
        current = addDays(current, 1);
      }
    });
    return dates;
  }

  private isDateBooked = (date: Date): boolean => {
    if (date < this.minDate) {
      return true
    }
    const dateStr = format(date, 'yyyy-MM-dd');
    return this.bookedDates.some(x => format(x, 'yyyy-MM-dd') === dateStr);
  };

  public dateFilter = (d: Date): boolean => {
    return !this.isDateBooked(d)
  };


}
