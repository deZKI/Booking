import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {UserRoutingModule} from "./user-routing.module";
import {FormsModule} from "@angular/forms";
import { LoginRegisterComponent } from './login-register/login-register.component';
import {MatIcon} from "@angular/material/icon";



@NgModule({
  declarations: [
    LoginRegisterComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    FormsModule,
    MatIcon
  ]
})
export class UserModule { }
