import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {HotelDetailComponent} from "./hotel-detail/hotel-detail.component";
import {FormsModule} from "@angular/forms";
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


@NgModule({
  declarations: [
    HotelDetailComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    MatIcon,
    MatButton,
    HotelRoutingModule,
    HttpClientModule,
    CarouselComponent,
    CarouselIndicatorsComponent,
    CarouselInnerComponent,
    CarouselControlComponent,
    CarouselItemComponent,
  ]
})
export class HotelModule {
}
