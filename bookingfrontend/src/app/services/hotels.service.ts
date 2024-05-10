import {Injectable} from '@angular/core';
import {Hotel, HotelDetail, RoomDetail, Service} from "../shared/models/hotels";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class HotelsService {

  private apiHotels = `${environment.apiUrl}/hotels/`
  private apiRooms = `${environment.apiUrl}/rooms/`
  private apiService = `${environment.apiUrl}/services/`

  constructor(private http: HttpClient) {
  }

  getHotels(): Observable<Hotel[]> {
    return this.http.get<Hotel[]>(this.apiHotels);
  }

  getHotelById(id: number): Observable<HotelDetail> {
    return this.http.get<HotelDetail>(this.apiHotels + id);
  }

  getRoomById(id: number): Observable<RoomDetail> {
    return this.http.get<RoomDetail>(this.apiRooms + id);
  }

  getServices(): Observable<Service[]> {
    return this.http.get<Service[]>(this.apiService);
  }
}
