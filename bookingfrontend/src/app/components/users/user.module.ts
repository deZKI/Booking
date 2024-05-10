import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {UserRoutingModule} from "./user-routing.module";
import {FormsModule} from "@angular/forms";
import { LoginRegisterComponent } from './login-register/login-register.component';
import {MatIcon} from "@angular/material/icon";
import { AccountComponent } from './account/account.component';
import {
  MatCard,
  MatCardActions,
  MatCardContent,
  MatCardHeader,
  MatCardSubtitle,
  MatCardTitle
} from "@angular/material/card";
import {MatList, MatListItem} from "@angular/material/list";
import {MatButton} from "@angular/material/button";



@NgModule({
  declarations: [
    LoginRegisterComponent,
    AccountComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    FormsModule,
    MatIcon,
    MatCardContent,
    MatCardSubtitle,
    MatCardTitle,
    MatCard,
    MatCardHeader,
    MatListItem,
    MatList,
    MatCardActions,
    MatButton
  ]
})
export class UserModule { }
