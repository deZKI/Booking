import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from "./components/shared/home/home.component";
import {HotelDetailComponent} from "./components/hotel/hotel-detail/hotel-detail.component";

const routes: Routes = [
  {path: '', component: HomeComponent, data: {breadcrumb: 'Главная'}},
  {path: 'hotels',
    loadChildren: () => import('./components/hotel/hotel.module').then(m => m.HotelModule),
  },
  {
    path: 'user',
    loadChildren: () => import('./components/users/user.module').then(m => m.UserModule),
    data: {breadcrumb: 'Личный кабинет'}
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
