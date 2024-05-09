import {Component, OnInit} from '@angular/core';
import {HotelDetail} from "../../../shared/models/hotels";
import {HotelsService} from "../../../services/hotels.service";
import {ActivatedRoute} from "@angular/router";
import {take, tap} from "rxjs";

@Component({
  selector: 'app-hotel-detail',
  templateUrl: './hotel-detail.component.html',
  styleUrl: './hotel-detail.component.scss'
})
export class HotelDetailComponent implements OnInit {
  hotel!: HotelDetail;
  hotelId!: number;

  constructor(
    private hotelService: HotelsService,
    private route: ActivatedRoute,
  ) {
  }

  ngOnInit() {
    this.hotelId = this.route.snapshot.params['id']
    this.hotelService.getHotelById(this.hotelId).pipe(
      take(1),
      tap(hotel => this.hotel = hotel)
    ).subscribe()
  }

  getStars(rating: number): any[] {
    return new Array(rating);
  }
}
