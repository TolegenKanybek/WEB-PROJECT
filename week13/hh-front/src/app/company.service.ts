import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Company,LoginResponse} from './company';
import {Vacancy} from './vacancy';




@Injectable({
    providedIn: 'root'
  })
  export class CompanyService {
  
    BASE_URL = 'http://localhost:8000';
    constructor(private http: HttpClient) {}
  
    getCompanyList(): Observable<Company[]> {
      return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
    }
  
    getCompany(id): Observable<Company> {
      return this.http.get<Company>(`${this.BASE_URL}/api/companies${id}/`);
    }
  
    deleteCompany(id): Observable<any> {
      return this.http.delete(`${this.BASE_URL}/api/companies/${id}/`);
    }
  
    getVacancyList(id): Observable<Vacancy[]> {
      return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
    }

    getVacancyDetail(id):Observable<Vacancy>{
      return this.http.get<Vacancy>(`${this.BASE_URL}/vacancies/${id}`)
    }

    getTopTenList():Observable<Vacancy[]>{
      return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies/top_ten`)
    }

    login(username, password): Observable<LoginResponse> {
        return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
          username:username,
          password:password
        });
      }
  }  