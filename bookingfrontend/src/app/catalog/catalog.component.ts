import {Component, OnInit} from '@angular/core';
import {Hotel} from "../models/hotels";
import {HotelsService} from "../services/hotels.service";
import {take, tap} from "rxjs";

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrl: './catalog.component.scss'
})
export class CatalogComponent implements OnInit {
  hotels: Hotel[] = [];

  constructor(private hotelsService: HotelsService) {
  }

  ngOnInit(): void {
    this.hotelsService.getHotels().pipe(
      take(1),
      tap(hotels => this.hotels = hotels)
    ).subscribe();
  }
}
