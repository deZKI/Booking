import {Component, OnInit} from '@angular/core';
import {RoomDetail} from "../../../shared/models/hotels";
import {HotelsService} from "../../../services/hotels.service";
import {ActivatedRoute, Router} from "@angular/router";
import {take, tap} from "rxjs";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

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

  constructor(
    private hotelService: HotelsService,
    private route: ActivatedRoute,
    private fb: FormBuilder
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
    this.initForm();
  }

  initForm() {
    this.bookingForm = this.fb.group({
      surname: ['', Validators.required],
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', [Validators.required, Validators.pattern(/^\d{10}$/)]],
      arrivalDate: ['', Validators.required],
      departureDate: ['', Validators.required]
    });
  }

  bookRoom() {
    console.log('Booking data:', this.bookingForm.value);
    if (this.bookingForm.valid) {
      // Логика отправки данных для бронирования
      console.log('Booking data:', this.bookingForm.value);
    }
  }

  getStars(rating: number): any[] {
    return new Array(rating);
  }

}
