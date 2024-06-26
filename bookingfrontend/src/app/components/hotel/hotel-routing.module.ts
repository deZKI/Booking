import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HotelDetailComponent} from "./hotel-detail/hotel-detail.component";
import {RoomDetailComponent} from "./room-detail/room-detail.component";
import {AuthGuard} from "../../auth.guard";

const routes: Routes = [
  {path: ':id', component: HotelDetailComponent, data: {breadcrumb: 'Отели'}},
  {path: ':hotelId/room/:roomId', component: RoomDetailComponent, data: {breadcrumb: 'Номера'}, canActivate: [AuthGuard] }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HotelRoutingModule {
}
