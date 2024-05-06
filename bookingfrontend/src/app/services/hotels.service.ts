import {Injectable} from '@angular/core';
import {Hotel} from "../shared/models/hotels";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class HotelsService {

  private apiUrl = `${environment.apiUrl}/hotels/`

  constructor(private http: HttpClient) {
  }

  getHotels(): Observable<Hotel[]> {
    return this.http.get<Hotel[]>(this.apiUrl);
  }

}
