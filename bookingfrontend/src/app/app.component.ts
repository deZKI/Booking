import {Component} from '@angular/core';
import {MatIconRegistry} from "@angular/material/icon";
import {DomSanitizer} from "@angular/platform-browser";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'bookingfrontend';

  constructor(
    private matIconRegistry: MatIconRegistry,
    private domSanitizer: DomSanitizer,
  ) {
    this.supplementMatIconRegistry();
  }

  private supplementMatIconRegistry() {
    this.matIconRegistry.addSvgIcon(
      `lagoona-logo`,
      this.domSanitizer.bypassSecurityTrustResourceUrl("/assets/icons/lagonalogo.svg")
    ).addSvgIcon(
      'arrow',
      this.domSanitizer.bypassSecurityTrustResourceUrl("/assets/icons/arrow.svg")
    ).addSvgIcon(
      'avatar',
      this.domSanitizer.bypassSecurityTrustResourceUrl("/assets/icons/avatar.svg")
    ).addSvgIcon(
      'enter-outline',
      this.domSanitizer.bypassSecurityTrustResourceUrl("/assets/icons/enter-outline.svg")
    )
  }
}
