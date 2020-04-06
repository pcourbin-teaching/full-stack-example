import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { environment } from '../environments/environment';
import { ApiModule } from '../../DebatIDOAPI/api.module';
import { BASE_PATH } from '../../DebatIDOAPI/variables';

import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatSliderModule } from '@angular/material/slider';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatTabsModule } from '@angular/material/tabs';
import { MatExpansionModule } from '@angular/material/expansion';

import { ThemeTableComponent } from './theme-table/theme-table.component';
import { ProtagonistTableComponent } from './protagonist-table/protagonist-table.component';
import { QuoteTableComponent } from './quote-table/quote-table.component';
import { ReferenceTableComponent } from './reference-table/reference-table.component';
import { QuoteGraphComponent } from './quote-graph/quote-graph.component';



@NgModule({
  declarations: [
    AppComponent,
    ThemeTableComponent,
    ProtagonistTableComponent,
    QuoteTableComponent,
    ReferenceTableComponent,
    QuoteGraphComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ApiModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatTableModule,
    MatTabsModule,
    MatPaginatorModule,
    MatSortModule,
    MatExpansionModule,
  ],
  providers: [ { provide: BASE_PATH, useValue: environment.API_BASE_PATH } ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
