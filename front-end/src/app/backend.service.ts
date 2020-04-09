import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {API_URL} from '../app/env';
import { Observable } from 'rxjs';

@Injectable()
export class BackendService {

  constructor(private http: HttpClient) {
  }



  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }


    // GET list of public, future events
    getSomething() {
      return this.http
        .get(`${API_URL}/employees`);
    }

}
