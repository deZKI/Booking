import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from "./components/home/home.component";
import {HotelDetailComponent} from "./components/hotel-detail/hotel-detail.component";

const routes: Routes = [
  {path: '', component: HomeComponent, data: {breadcrumb: 'Главная'}},
  {path: 'hotels/:id', component: HotelDetailComponent, data: {breadcrumb: 'Отели'}},
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
