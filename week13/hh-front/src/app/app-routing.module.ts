import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyListComponent} from './company-list/company-list.component';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';
import { AppComponent } from './app.component';

const routes: Routes = [
  { path: '', component: CompanyListComponent },
  { path: 'companies/:id', component: VacancyListComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
