import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {RegistrationComponent} from './registration/registration.component';
import {LoginComponent} from "./login/login.component";

const routes: Routes = [
  {path: 'register', component: RegistrationComponent, data: { breadcrumb: 'Регистрация' }},
  {path: 'login', component: LoginComponent, data: { breadcrumb: 'Авторизация' }}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule {
}
