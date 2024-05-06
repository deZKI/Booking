import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {LoginRegisterComponent} from "./login-register/login-register.component";
import {AuthGuard} from "../../auth.guard";

const routes: Routes = [
  {path: 'register', component: LoginRegisterComponent, data: {breadcrumb: 'Регистрация'}},
  {path: 'login', component: LoginRegisterComponent, data: {breadcrumb: 'Авторизация'}}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule {
}
