import {Component, Input} from '@angular/core';
import {Hotel} from "../../shared/models/hotels";

@Component({
  selector: 'app-hotel-card',
  templateUrl: './hotel-card.component.html',
  styleUrl: './hotel-card.component.scss'
})
export class HotelCardComponent {
  @Input() hotel!: Hotel;
}
