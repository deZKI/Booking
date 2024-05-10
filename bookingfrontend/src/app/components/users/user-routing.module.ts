import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {LoginRegisterComponent} from "./login-register/login-register.component";
import {AuthGuard} from "../../auth.guard";
import {AccountComponent} from "./account/account.component";

const routes: Routes = [
  {path: '', component: AccountComponent, data: {breadcrumb: ''}, canActivate: [AuthGuard] },
  {path: 'register', component: LoginRegisterComponent, data: {breadcrumb: 'Регистрация'}},
  {path: 'login', component: LoginRegisterComponent, data: {breadcrumb: 'Авторизация'}}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule {
}
