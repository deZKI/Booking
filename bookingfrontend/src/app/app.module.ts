import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {NavbarComponent} from './components/shared/navbar/navbar.component';
import {provideAnimationsAsync} from '@angular/platform-browser/animations/async';
import {MatIcon} from "@angular/material/icon";
import {MatButton} from "@angular/material/button";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import { FooterComponent } from './components/shared/footer/footer.component';
import { BreadcrumbsComponent } from './components/shared/breadcrumbs/breadcrumbs.component';
import { HomeComponent } from './components/shared/home/home.component';
import { CatalogComponent } from './components/shared/catalog/catalog.component';
import { HotelCardComponent } from './components/shared/catalog/hotel-card/hotel-card.component';
import {AuthInterceptor} from "./auth.interceptor";
import {AuthGuard} from "./auth.guard";
import {AuthService} from "./services/auth.service";
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    BreadcrumbsComponent,
    HomeComponent,
    CatalogComponent,
    HotelCardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatIcon,
    MatButton,
    HttpClientModule
  ],
  providers: [
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
