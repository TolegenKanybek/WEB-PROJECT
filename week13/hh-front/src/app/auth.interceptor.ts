import {HttpEvent, HttpHandler, HttpInterceptor, HttpRequest} from '@angular/common/http';
import {Observable} from 'rxjs/internal/Observable';
import {Injectable} from '@angular/core';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    
    const token = localStorage.getItem('token');
    if (token) {
      console.log('we have token in local storage');
      //console.log('re')
      const authReq = req.clone({
        headers: req.headers.append('Authorization', `JWT ${token}`)
      });
      return next.handle(authReq);
    }
    console.log('no token in local storage');
    return next.handle(req);
  }
}