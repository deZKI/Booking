import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HotelDetailComponent} from "./hotel-detail/hotel-detail.component";

const routes: Routes = [
  {path: ':id', component: HotelDetailComponent, data: {breadcrumb: 'Отели'}},
  {path: ':id/room:id/', component: HotelDetailComponent, data: {breadcrumb: 'Отели'}},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HotelRoutingModule {
}
