import {Component, Input} from '@angular/core';
import {Hotel} from "../../shared/models/hotels";
import {Router} from "@angular/router";

@Component({
  selector: 'app-hotel-card',
  templateUrl: './hotel-card.component.html',
  styleUrl: './hotel-card.component.scss'
})
export class HotelCardComponent {
  @Input() hotel!: Hotel;

  constructor(private router: Router,) {
  }

  getStars(rating: number): any[] {
    return new Array(rating);
  }

  navigateToHotelDetail() {
    this.router.navigate(['/hotels/' + this.hotel.id]);
  }
}
