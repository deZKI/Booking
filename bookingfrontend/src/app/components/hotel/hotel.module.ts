import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {HotelDetailComponent} from "./hotel-detail/hotel-detail.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatIcon} from "@angular/material/icon";
import {MatButton} from "@angular/material/button";
import {HttpClientModule} from "@angular/common/http";
import {HotelRoutingModule} from "./hotel-routing.module";
import {
  CarouselComponent,
  CarouselControlComponent,
  CarouselIndicatorsComponent,
  CarouselInnerComponent, CarouselItemComponent
} from "@coreui/angular";
import { RoomDetailComponent } from './room-detail/room-detail.component';
import {MatNativeDateModule} from "@angular/material/core";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {MatDatepickerModule} from "@angular/material/datepicker";


@NgModule({
  declarations: [
    HotelDetailComponent,
    RoomDetailComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    MatIcon,
    MatButton,
    MatDatepickerModule,
    MatInputModule,
    MatFormFieldModule,
    MatNativeDateModule,
    HotelRoutingModule,
    HttpClientModule,
    CarouselComponent,
    CarouselIndicatorsComponent,
    CarouselInnerComponent,
    CarouselControlComponent,
    CarouselItemComponent,
    ReactiveFormsModule,
  ]
})
export class HotelModule {
}
