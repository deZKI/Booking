import {Component} from '@angular/core';
import {Router} from '@angular/router';
import {AuthService} from "../../../services/auth.service";


@Component({
  selector: 'app-login-register',
  templateUrl: './login-register.component.html',
  styleUrl: './login-register.component.scss'
})
export class LoginRegisterComponent {
  email = '';
  password = '';
  isLoginMode = true;
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {
  }

  toggleMode(): void {
    this.isLoginMode = !this.isLoginMode;
    this.errorMessage = '';
  }

  onSubmit(): void {
    this.errorMessage = '';

    if (this.isLoginMode) {
      this.authService.login(this.email, this.password).subscribe(() => {
        let returnUrl = localStorage.getItem('returnUrl') || '/';
        localStorage.removeItem('returnUrl');
        this.router.navigateByUrl(returnUrl);
      }, error => {
        this.errorMessage = 'Ошибка входа. Проверьте ваши учетные данные.';
      });
    } else {
      this.authService.register(this.email, this.password).subscribe(() => {
        this.router.navigate(['/']);
      }, error => {
        this.errorMessage = 'Ошибка регистрации. Проверьте ваши учетные данные.';
      });
    }
  }
}
